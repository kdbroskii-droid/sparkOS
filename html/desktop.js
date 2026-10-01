const appWindow=document.getElementById("appWindow");
const windowTitle=document.getElementById("windowTitle");
const windowBody=document.getElementById("windowBody");
const startMenu=document.getElementById("startMenu");
const zapButton=document.getElementById("zapButton");

const apps={
 files:{title:"Files",body:'<h2>Files</h2><p>Your files and folders.</p><div class="file-list"><div class="file-row">Home</div><div class="file-row">Downloads</div><div class="file-row">Documents</div><div class="file-row">Pictures</div></div>'},
 browser:{title:"Browser",body:'<div class="browser-page"><div><h2>Browser</h2><p>SparkOS web browser</p></div></div>'},
 terminal:{title:"Terminal",body:'<h2>Terminal</h2><p>SparkOS command terminal</p><div class="file-row">sparkOS@desktop:~$</div>'},
 store:{title:"App Store",body:'<h2>App Store</h2><p>Install trusted SparkOS applications.</p>'},
 settings:{title:"Settings",body:'<h2>Settings</h2><p>System settings and personalization.</p>'}
};

function openApp(name){
 const app=apps[name]; if(!app)return;
 windowTitle.textContent=app.title;
 windowBody.innerHTML=app.body;
 appWindow.classList.add("open");
 startMenu.classList.remove("open");
 zapButton.classList.remove("active");
}
function closeApp(){appWindow.classList.remove("open")}
function toggleStart(){
 const open=startMenu.classList.toggle("open");
 zapButton.classList.toggle("active",open);
}
document.querySelectorAll("[data-app]").forEach(button=>button.addEventListener("click",()=>openApp(button.dataset.app)));
document.getElementById("closeWindow").addEventListener("click",closeApp);
zapButton.addEventListener("click",toggleStart);
document.addEventListener("click",event=>{
 if(!startMenu.contains(event.target)&&!zapButton.contains(event.target))startMenu.classList.remove("open");
});
function updateClock(){
 const now=new Date();
 document.getElementById("time").textContent=now.toLocaleTimeString([], {hour:"2-digit",minute:"2-digit"});
 document.getElementById("date").textContent=now.toLocaleDateString([], {day:"2-digit",month:"short"});
}
updateClock();setInterval(updateClock,1000);
