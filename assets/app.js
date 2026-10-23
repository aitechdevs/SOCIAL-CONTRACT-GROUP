'use strict';
const menu=document.querySelector('.menu-toggle'),nav=document.querySelector('#navigation');
menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Close navigation':'Open navigation');nav.classList.toggle('open',open);});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav?.classList.contains('open')){menu.click();menu.focus();}});
const slides=[
 {title:'A stronger Nigeria.<br>A shared responsibility.',description:'Progress begins with an informed people. Connecting citizens, public policy and the possibilities of a better Nigeria.',label:'Discover our purpose',page:'about',art:'assets/photos/community-skyline.webp',alt:'Illustrative scene of a diverse group overlooking a city'},
 {title:'Opportunity begins<br>with understanding.',description:'Explore education, student finance and the public policies that shape access to opportunity.',label:'Explore education & policy',page:'achievements',art:'assets/photos/students-library.webp',alt:'Illustrative scene of students discussing coursework in a library'},
 {title:'Understand energy.<br>Ask better questions.',description:'Explore electricity regulation, generation and distribution through public policy resources.',label:'Explore energy resources',page:'news',art:'assets/photos/energy-engineers.webp',alt:'Illustrative scene of engineers beside solar panels and electricity pylons'},
 {title:'Connect communities.<br>Follow the progress.',description:'Take a closer look at infrastructure, public investment and the evidence behind delivery.',label:'Visit the project library',page:'projects',art:'assets/photos/bridge-construction.webp',alt:'Illustrative scene of a coastal bridge under construction'}
];
const title=document.querySelector('#slide-title');
if(title){let index=0,paused=matchMedia('(prefers-reduced-motion: reduce)').matches;const pause=document.querySelector('#pause-slider');let timer;
 function update(){const s=slides[index];title.innerHTML=s.title;document.querySelector('#slide-description').textContent=s.description;const link=document.querySelector('#slide-link');link.innerHTML=s.label+' <span class="outbound" aria-hidden="true"></span>';link.href='index.php?page='+s.page;document.querySelector('#slide-number').textContent=String(index+1).padStart(2,'0');document.querySelector('.slide-track i').style.width=((index+1)*25)+'%';const hero=document.querySelector('#hero-photo');hero.src=s.art;hero.alt=s.alt;document.querySelector('.hero-copy').classList.remove('fade-in');requestAnimationFrame(()=>document.querySelector('.hero-copy').classList.add('fade-in'));}
 function schedule(){clearInterval(timer);if(!paused)timer=setInterval(()=>{index=(index+1)%4;update();},8000);}
 document.querySelectorAll('[data-direction]').forEach(b=>b.addEventListener('click',()=>{index=(index+Number(b.dataset.direction)+4)%4;update();schedule();}));
 pause.textContent=paused?'▷':'Ⅱ';pause.setAttribute('aria-label',paused?'Play slideshow':'Pause slideshow');pause.addEventListener('click',()=>{paused=!paused;pause.textContent=paused?'▷':'Ⅱ';pause.setAttribute('aria-label',paused?'Play slideshow':'Pause slideshow');schedule();});
 document.querySelector('.hero').addEventListener('focusin',()=>clearInterval(timer));document.querySelector('.hero').addEventListener('focusout',schedule);document.addEventListener('visibilitychange',()=>document.hidden?clearInterval(timer):schedule());schedule();
}
document.querySelector('#project-filter')?.addEventListener('change',e=>{let count=0;document.querySelectorAll('[data-category]').forEach(c=>{c.hidden=e.target.value!=='all'&&c.dataset.category!==e.target.value;if(!c.hidden)count++;});document.querySelector('#result-count').textContent=count+' policy area'+(count===1?'':'s');});
document.querySelector('#state-search')?.addEventListener('input',e=>{let count=0;document.querySelectorAll('[data-state]').forEach(c=>{c.hidden=!c.dataset.state.includes(e.target.value.trim().toLowerCase());if(!c.hidden)count++;});document.querySelector('#state-count').textContent=count+' location'+(count===1?'':'s');document.querySelector('#no-states').hidden=count!==0;});
document.querySelector('#show-password')?.addEventListener('click',e=>{const p=document.querySelector('#password'),show=p.type==='password';p.type=show?'text':'password';e.target.textContent=show?'Hide':'Show';e.target.setAttribute('aria-label',show?'Hide password':'Show password');});

const resourceFilters=document.querySelectorAll('[data-resource-filter]');
resourceFilters.forEach(button=>button.addEventListener('click',()=>{
 resourceFilters.forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
 let count=0;document.querySelectorAll('.resource-grid [data-resource-category]').forEach(card=>{card.hidden=button.dataset.resourceFilter!=='all'&&card.dataset.resourceCategory!==button.dataset.resourceFilter;if(!card.hidden)count++;});
 document.querySelector('#resource-count').textContent=count+' topic guide'+(count===1?'':'s');
}));
