'use strict';
(() => {
 const hero=document.querySelector('.homepage-hero');
 if(!hero)return;
 let slides;
 try{slides=JSON.parse(hero.dataset.slides);}catch{return;}
 if(!Array.isArray(slides)||slides.length<2)return;
 const frames=[...hero.querySelectorAll('.slide-frame')];
 const pause=hero.querySelector('#pause-slider');
 const counter=hero.querySelector('#slide-number');
 const progress=hero.querySelector('.slide-track i');
 const status=hero.querySelector('.slider-status');
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 let index=0,active=0,userPaused=reduced.matches,focusWithin=false,hovered=false,timer,loading=false;
 const cache=new Map();
 const canPlay=()=>!userPaused&&!document.hidden&&!focusWithin&&!hovered;
 function preload(src){
  if(cache.has(src))return cache.get(src);
  const task=new Promise((resolve,reject)=>{
   const image=new Image();
   const timeout=setTimeout(()=>reject(new Error('Image loading timed out')),15000);
   image.onload=async()=>{clearTimeout(timeout);try{await image.decode();}catch{}resolve(src);};
   image.onerror=()=>{clearTimeout(timeout);reject(new Error('Image unavailable'));};
   image.src=src;
  }).catch(error=>{cache.delete(src);throw error;});
  cache.set(src,task);return task;
 }
 function updatePause(){
  const path=userPaused?'<path d="M5 3l10 7-10 7z"/>':'<path d="M5 3h4v14H5zm7 0h4v14h-4z"/>';
  pause.innerHTML='<svg viewBox="0 0 20 20" aria-hidden="true">'+path+'</svg>';
  pause.setAttribute('aria-label',userPaused?'Play slideshow':'Pause slideshow');
  pause.setAttribute('aria-pressed',String(userPaused));
 }
 function schedule(){
  clearTimeout(timer);hero.dataset.paused=String(!canPlay());
  if(canPlay()&&!loading)timer=setTimeout(()=>show(index+1),8000);
 }
 async function show(target,manual=false){
  if(loading)return;
  target=(target+slides.length)%slides.length;
  if(target===index)return;
  loading=true;clearTimeout(timer);hero.setAttribute('aria-busy','true');
  try{
   const src=await preload(slides[target].src);
   const next=1-active;
   frames[next].src=src;frames[next].alt=slides[target].alt;
   frames[next].setAttribute('aria-hidden','false');
   // Decode the actual display element before beginning the fade.
   try{await frames[next].decode();}catch{}
   frames[active].style.transform=getComputedStyle(frames[active]).transform;
   frames[active].classList.remove('is-active');frames[active].setAttribute('aria-hidden','true');frames[active].alt='';
   frames[next].classList.add('is-active');
   active=next;index=target;
   hero.querySelector('#slide-caption-title').textContent=slides[target].title;
   hero.querySelector('#slide-caption-description').textContent=slides[target].description;
   if(!reduced.matches)hero.querySelector('.slide-caption').animate([{opacity:0,transform:'translateY(14px)'},{opacity:1,transform:'translateY(0)'}],{duration:650,easing:'ease-out'});
   counter.textContent=String(index+1).padStart(2,'0');progress.style.width=((index+1)/slides.length*100)+'%';
   if(manual)status.textContent='Slide '+(index+1)+' of '+slides.length;
   await new Promise(resolve=>setTimeout(resolve,reduced.matches?0:950));
  }catch{status.textContent='This image could not load. The current slide is still available.';}
  finally{loading=false;hero.setAttribute('aria-busy','false');schedule();}
 }
 hero.querySelectorAll('[data-direction]').forEach(button=>button.addEventListener('click',()=>show(index+Number(button.dataset.direction),true)));
 pause.addEventListener('click',()=>{userPaused=!userPaused;updatePause();schedule();});
 hero.addEventListener('keydown',event=>{if(event.key==='ArrowLeft'||event.key==='ArrowRight'){event.preventDefault();show(index+(event.key==='ArrowLeft'?-1:1),true);}});
 hero.addEventListener('focusin',()=>{focusWithin=true;schedule();});
 hero.addEventListener('focusout',()=>queueMicrotask(()=>{focusWithin=hero.contains(document.activeElement);schedule();}));
 hero.addEventListener('mouseenter',()=>{hovered=true;schedule();});hero.addEventListener('mouseleave',()=>{hovered=false;schedule();});
 document.addEventListener('visibilitychange',schedule);
 reduced.addEventListener('change',()=>{if(reduced.matches)userPaused=true;updatePause();schedule();});
 let touch;
 hero.addEventListener('pointerdown',event=>{if(event.pointerType==='touch')touch={x:event.clientX,y:event.clientY};},{passive:true});
 hero.addEventListener('pointerup',event=>{if(!touch)return;const dx=event.clientX-touch.x,dy=event.clientY-touch.y;touch=null;if(Math.abs(dx)>55&&Math.abs(dx)>Math.abs(dy)*1.4)show(index+(dx<0?1:-1),true);},{passive:true});
 const sizeHero=()=>hero.style.setProperty('--hero-offset',Math.round(hero.getBoundingClientRect().top+window.scrollY)+'px');
 sizeHero();window.addEventListener('resize',sizeHero);
 if('ResizeObserver' in window){const observer=new ResizeObserver(sizeHero);document.querySelectorAll('header,.utility,.topic-nav').forEach(el=>observer.observe(el));}
 updatePause();schedule();
 const warm=()=>slides.slice(1).forEach(slide=>preload(slide.src).catch(()=>{}));
 if('requestIdleCallback' in window)requestIdleCallback(warm,{timeout:2500});else setTimeout(warm,1500);
})();
