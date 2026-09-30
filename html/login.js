const emailButton=document.getElementById("emailButton");
const googleButton=document.getElementById("googleButton");
const phoneButton=document.getElementById("phoneButton");
const guestButton=document.getElementById("guestButton");
const loginOptions=document.getElementById("loginOptions");
const emailForm=document.getElementById("emailForm");
const phonePanel=document.getElementById("phonePanel");
const backButtons=document.querySelectorAll("[data-back]");
const status=document.getElementById("status");
const emailInput=document.getElementById("email");
const passwordInput=document.getElementById("password");
const usernameInput=document.getElementById("username");

function showEmail(){
 loginOptions.style.display="none";
 emailForm.classList.add("show");
 phonePanel.classList.remove("show");
 emailInput.focus();
}
function showPhone(){
 loginOptions.style.display="none";
 emailForm.classList.remove("show");
 phonePanel.classList.add("show");
 status.textContent="";
}
function resetLogin(){
 loginOptions.style.display="grid";
 emailForm.classList.remove("show");
 phonePanel.classList.remove("show");
 status.textContent="";
}
function openAccount(email,username,password){
 if(!email){status.textContent="Enter your email address.";return}
 const accountKey="sparkos-account-"+email.toLowerCase().trim();
 const saved=localStorage.getItem(accountKey);
 if(!saved){
   if(!username){status.textContent="Create a username for this account.";return}
   localStorage.setItem(accountKey,JSON.stringify({email:email.toLowerCase().trim(),username,password:password||"",created:true}));
   status.textContent="Account created. Opening SparkOS…";
   setTimeout(()=>alert("Logged in as "+username),350);
   return;
 }
 const account=JSON.parse(saved);
 if(account.password===""){
   if(password===" " || password===""){status.textContent="Account opened with Space.";setTimeout(()=>alert("Logged in as "+account.username),250);return}
 }
 if(password!==account.password){status.textContent="Incorrect password.";return}
 status.textContent="Login successful.";
 setTimeout(()=>alert("Logged in as "+account.username),250);
}
emailButton.addEventListener("click",showEmail);
googleButton.addEventListener("click",()=>{status.textContent="Google sign-in will use secure Google OAuth in the real SparkOS build.";});
phoneButton.addEventListener("click",showPhone);
guestButton.addEventListener("click",()=>alert("Guest Mode opened."));
backButtons.forEach(b=>b.addEventListener("click",resetLogin));
emailForm.addEventListener("submit",event=>{
 event.preventDefault();
 const email=emailInput.value.trim();
 const username=usernameInput.value.trim();
 const password=passwordInput.value;
 openAccount(email,username,password);
});
passwordInput.addEventListener("keydown",event=>{
 if(event.key===" " && passwordInput.value===""){
   event.preventDefault();
   openAccount(emailInput.value.trim(),usernameInput.value.trim()," ");
 }
});
