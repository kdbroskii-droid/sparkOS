const appWindow=document.getElementById("appWindow");
const windowTitle=document.getElementById("windowTitle");
const windowBody=document.getElementById("windowBody");
const startMenu=document.getElementById("startMenu");
const zapButton=document.getElementById("zapButton");

const apps={
 files:{title:"Files",body:'<h2>Files</h2><p>Your files and folders.</p><div class="file-list"><div class="file-row">Home</div><div class="file-row">Downloads</div><div class="file-row">Documents</div><div class="file-row">Pictures</div></div>'},
 browser:{title:"Browser",body:'<div class="browser-page"><div><h2>Browser</h2><p>SparkOS web browser</p></div></div>'},
 terminal:{title:"Terminal",body:'<h2>Terminal</h2><p>SparkOS command terminal</p><div class="file-row">sparkOS@desktop:~$</div>'},
 store:{title:"App Store",body:'<iframe src="app-store-test.html" title="SparkOS App Store" style="width:100%;height:100%;border:0;border-radius:12px;background:#0d1622"></iframe>'},
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

/* Physical Chromebook/SparkOS keyboard mappings.
   The finished OS should connect these actions to its native power,
   display, audio and media services instead of using browser APIs. */
const keyActions={
 "AudioVolumeUp":()=>showKeyStatus("Volume up"),
 "AudioVolumeDown":()=>showKeyStatus("Volume down"),
 "AudioVolumeMute":()=>showKeyStatus("Mute"),
 "BrightnessUp":()=>showKeyStatus("Brightness up"),
 "BrightnessDown":()=>showKeyStatus("Brightness down"),
 "MediaPlayPause":()=>showKeyStatus("Play / pause"),
 "MediaTrackNext":()=>showKeyStatus("Next track"),
 "MediaTrackPrevious":()=>showKeyStatus("Previous track"),
 "LaunchSearch":()=>toggleStart(),
 "Search":()=>toggleStart(),
 "Escape":()=>{if(startMenu.classList.contains("open"))startMenu.classList.remove("open");else closeApp()},
 "BrowserBack":()=>showKeyStatus("Back"),
 "BrowserForward":()=>showKeyStatus("Forward"),
 "BrowserRefresh":()=>showKeyStatus("Refresh")
};

function showKeyStatus(message){
 const status=document.getElementById("keyStatus");
 if(!status)return;
 status.textContent=message;
 status.classList.add("show");
 clearTimeout(window.sparkKeyStatusTimer);
 window.sparkKeyStatusTimer=setTimeout(()=>status.classList.remove("show"),900);
}

document.addEventListener("keydown",event=>{
 const action=keyActions[event.key];
 if(action){
   event.preventDefault();
   action();
   return;
 }
 if(event.key==="F11"){
   event.preventDefault();
   showKeyStatus("Fullscreen");
 }
});

/* Hardware-only keys.
   These are intentionally not simulated in the browser:
   - Power button: native OS power manager
   - Sleep/wake: native OS power manager
   - Hardware lid close: native OS power manager
*/
function handleNativePowerEvent(action){
 window.dispatchEvent(new CustomEvent("sparkos-power",{detail:{action}}));
}
window.handleNativePowerEvent=handleNativePowerEvent;

function updateClock(){
 const now=new Date();
 document.getElementById("time").textContent=now.toLocaleTimeString([], {hour:"2-digit",minute:"2-digit"});
 document.getElementById("date").textContent=now.toLocaleDateString([], {day:"2-digit",month:"short"});
}
updateClock();setInterval(updateClock,1000);
