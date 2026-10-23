'use strict';
const menu=document.querySelector('.menu-toggle'),nav=document.querySelector('#navigation');
menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Close navigation':'Open navigation');nav.classList.toggle('open',open);});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav?.classList.contains('open')){menu.click();menu.focus();}});
document.querySelector('#project-filter')?.addEventListener('change',e=>{let count=0;document.querySelectorAll('[data-category]').forEach(c=>{c.hidden=e.target.value!=='all'&&c.dataset.category!==e.target.value;if(!c.hidden)count++;});document.querySelector('#result-count').textContent=count+' policy area'+(count===1?'':'s');});
document.querySelector('#state-search')?.addEventListener('input',e=>{let count=0;document.querySelectorAll('[data-state]').forEach(c=>{c.hidden=!c.dataset.state.includes(e.target.value.trim().toLowerCase());if(!c.hidden)count++;});document.querySelector('#state-count').textContent=count+' location'+(count===1?'':'s');document.querySelector('#no-states').hidden=count!==0;});
document.querySelector('#show-password')?.addEventListener('click',e=>{const p=document.querySelector('#password'),show=p.type==='password';p.type=show?'text':'password';e.target.textContent=show?'Hide':'Show';e.target.setAttribute('aria-label',show?'Hide password':'Show password');});

const resourceFilters=document.querySelectorAll('[data-resource-filter]');
resourceFilters.forEach(button=>button.addEventListener('click',()=>{
 resourceFilters.forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
 let count=0;document.querySelectorAll('.resource-grid [data-resource-category]').forEach(card=>{card.hidden=button.dataset.resourceFilter!=='all'&&card.dataset.resourceCategory!==button.dataset.resourceFilter;if(!card.hidden)count++;});
 document.querySelector('#resource-count').textContent=count+' topic guide'+(count===1?'':'s');
}));
