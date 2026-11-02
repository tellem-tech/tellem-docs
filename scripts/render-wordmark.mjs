import fs from 'node:fs/promises';
import assert from 'node:assert/strict';
import {join,resolve} from 'node:path';
import {spawn} from 'node:child_process';
import {parseArgs} from 'node:util';
import {fileURLToPath,pathToFileURL} from 'node:url';

const usage='Usage: node scripts/render-wordmark.mjs --workshop ../tellem-workshop --output site/wordmark-rebuild';
const {values}=parseArgs({options:{workshop:{type:'string'},output:{type:'string'},help:{type:'boolean'}}});
if(values.help){console.log(usage);process.exit(0);}
assert.ok(values.workshop&&values.output,usage);
const {chromium}=await import(pathToFileURL(join(resolve(values.workshop),'node_modules/playwright/index.mjs')).href);
const work=resolve(values.output);await fs.mkdir(work,{recursive:true});
const source=await fs.readFile(fileURLToPath(new URL('../docs/media/logo.svg',import.meta.url)),'utf8');
const palette=await fs.readFile(fileURLToPath(new URL('../docs/css/extra.css',import.meta.url)),'utf8');
const accent=palette.match(/--tellem-brand:\s*(#[0-9a-f]{6})\s*;/i)?.[1];
assert.ok(accent,'Expected a six-digit --tellem-brand color in extra.css');
const paths=[...source.matchAll(/<path d="([^"]+)"/g)].slice(0,9).map(match=>match[1]);
assert.equal(paths.length,9);
// Six glyphs: the fourth letter uses two paths; paths 7 and 8 form the accent.
const letters=[[0],[1],[2],[3,4],[5],[6]];
const themes={light:{paper:'#ffffff',ink:'#25212c',gif:'tellem-wordmark-fall.gif',svg:'tellem-wordmark.svg'},dark:{paper:'#1e2129',ink:'#f3f0fa',gif:'tellem-wordmark-fall-dark.gif',svg:'tellem-wordmark-dark.svg'}};
const fps=50,duration=4,frameCount=fps*duration;
const mark=(config)=>`<svg xmlns="http://www.w3.org/2000/svg" width="640" height="250" viewBox="0 0 640 250" role="img" aria-label="Tellem"><title>Tellem</title><rect width="640" height="250" fill="${config.paper}"/><g transform="translate(105 39.767857142857) scale(1.535714285714)">${letters.map((group,index)=>`<g data-letter="${index}" fill="${config.ink}">${group.map(id=>`<path d="${paths[id]}"/>`).join('')}</g>`).join('')}<g data-accent="" fill="${accent}"><path d="${paths[7]}"/><path d="${paths[8]}"/></g></g></svg>`;
const run=(command,args)=>new Promise((yes,no)=>{const child=spawn(command,args,{stdio:['ignore','pipe','pipe']});const stdout=[],stderr=[];child.stdout.on('data',data=>stdout.push(data));child.stderr.on('data',data=>stderr.push(data));child.on('error',no);child.on('close',code=>code===0?yes(Buffer.concat(stdout)):no(new Error(Buffer.concat(stderr).toString())));});
const browser=await chromium.launch({headless:true});
const reports=[];
try{
 const page=await browser.newPage({viewport:{width:640,height:250},deviceScaleFactor:1});
 const errors=[];page.on('pageerror',error=>errors.push(error.message));
 for(const [theme,config]of Object.entries(themes)){
  const svg=mark(config),svgPath=join(work,config.svg),dir=join(work,'frames',theme);await fs.mkdir(dir,{recursive:true});
  assert.deepEqual([...svg.matchAll(/<path d="([^"]+)"/g)].map(match=>match[1]),paths,'native geometry retained');
  await fs.writeFile(svgPath,svg+'\n');
  await page.setContent('<style>html,body{margin:0;overflow:hidden}svg{display:block;overflow:hidden}</style>'+svg);
  const still=await page.screenshot();await fs.writeFile(join(dir,'static.png'),still);
  await page.evaluate(()=>{
   window.fallLogoFrame=(seconds)=>{
    const falling=progress=>{
     if(progress<=0)return -130;
     if(progress<.65)return -130*(1-Math.pow(progress/.65,2));
     if(progress<.82)return -5*Math.sin((progress-.65)/.17*Math.PI);
     if(progress<1)return -1.2*Math.sin((progress-.82)/.18*Math.PI);
     return 0;
    };
    const positions=[];
    document.querySelectorAll('[data-letter]').forEach((letter,index)=>{
     const y=falling((seconds-index*.19)/.66);positions.push(y);if(y===0)letter.removeAttribute('transform');else letter.setAttribute('transform',`translate(0 ${y})`);
    });
    const progress=Math.max(0,Math.min(1,(seconds-1.64)/.38)),settle=1-Math.pow(1-progress,3),accent=document.querySelector('[data-accent]');
    if(progress===1){accent.removeAttribute('style');accent.removeAttribute('transform');}else{accent.style.fillOpacity=String(settle);accent.setAttribute('transform',`translate(0 ${-16*(1-settle)})`);}
    return positions;
   };
  });
  const frames=[];
  for(let frame=0;frame<frameCount;frame++){
   const positions=await page.evaluate(seconds=>window.fallLogoFrame(seconds),frame/fps);
   if(frame===fps*.7){assert.ok(positions[0]===0&&positions[1]!==0,'first letter lands before the next');assert.ok(positions[5]<-100,'last letter has not fallen with the first');}
   const png=await page.screenshot();frames.push(png);await fs.writeFile(join(dir,String(frame).padStart(3,'0')+'.png'),png);
  }
  assert.ok(frames[3*fps].equals(frames.at(-1)),'final hold is still');
  assert.ok(!frames[.4*fps].equals(frames[fps]),'falling changes real pixels');
  const gifPath=join(work,config.gif);
  await run('ffmpeg',['-v','error','-framerate',String(fps),'-i',join(dir,'%03d.png'),'-filter_complex','[0:v]split[a][b];[a]palettegen=stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a','-loop','-1','-y',gifPath]);
  const bytes=await fs.readFile(gifPath);assert.equal(bytes.includes(Buffer.from('NETSCAPE2.0')),false,'GIF plays once');
  const probe=JSON.parse((await run('ffprobe',['-v','error','-count_frames','-show_entries','stream=width,height,nb_read_frames:format=duration,size','-of','json',gifPath])).toString());
  assert.equal(probe.streams[0].width,640);assert.equal(probe.streams[0].height,250);assert.equal(Number(probe.streams[0].nb_read_frames),frameCount);assert.equal(Number(probe.format.duration),duration);
  await run('ffmpeg',['-v','error','-i',gifPath,'-f','null','-']);
  const raw=await run('ffmpeg',['-v','error','-i',gifPath,'-vf',`select=eq(n\\,${frameCount-1})`,'-frames:v','1','-f','rawvideo','-pix_fmt','rgb24','pipe:1']);
  const native=await run('ffmpeg',['-v','error','-i',join(dir,'static.png'),'-f','rawvideo','-pix_fmt','rgb24','pipe:1']);
  assert.equal(raw.length,native.length);let square=0;for(let index=0;index<raw.length;index++)square+=Math.pow(raw[index]-native[index],2);
  const psnr=10*Math.log10(255*255/(square/raw.length));assert.ok(psnr>38,'indexed GIF retains native final contour detail');
  const expected=theme==='light'?[255,255,255]:[30,33,41];assert.deepEqual([...raw.subarray(0,3)],expected,'matte matches the homepage stage');
  await page.setViewportSize({width:320,height:150});
  await page.setContent(`<style>html,body{margin:0}img{display:block;width:260px;height:auto;max-width:100%}</style><img alt="Tellem" src="data:image/svg+xml;base64,${Buffer.from(svg).toString('base64')}">`);
  const image=page.locator('img');await image.evaluate(image=>image.decode());
  const bounds=await image.boundingBox();assert.ok(Math.abs(bounds.width-260)<1&&Math.abs(bounds.height-101.5625)<1,'mobile logo preserves its intrinsic ratio');
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await image.screenshot({path:join(dir,'mobile.png')});await page.setViewportSize({width:640,height:250});
  reports.push({theme,gif:config.gif,svg:config.svg,width:640,height:250,fps,frames:frameCount,duration,playback:'once, quiet final hold',psnr,bytes:bytes.length});
 }
 assert.deepEqual(errors,[]);
 await fs.writeFile(join(work,'checks.json'),JSON.stringify({timing:{letterDelay:.19,fallAndSettle:.66,accentStart:1.64,accentEnd:2.02,quietHoldFrom:2.02},reports},null,2)+'\n');
 console.log(JSON.stringify({ok:true,reports}));
}finally{await browser.close();}
