#!/usr/bin/env python3
import base64,getpass,hashlib,json,os,secrets,sys
from pathlib import Path
DB=Path("/var/lib/sparkos/accounts.json")
ITER=310000
def load():
    try:return json.loads(DB.read_text())
    except Exception:return {}
def save(db):
    DB.parent.mkdir(parents=True,exist_ok=True);os.chmod(DB.parent,0o700);DB.write_text(json.dumps(db,indent=2));os.chmod(DB,0o600)
def add(name,password):
    db=load()
    if name in db:raise SystemExit("Account already exists")
    salt=secrets.token_bytes(16)
    db[name]={"salt":base64.b64encode(salt).decode(),"hash":base64.b64encode(hashlib.pbkdf2_hmac("sha256",password.encode(),salt,ITER)).decode()}
    save(db)
def check(name,password):
    a=load().get(name)
    if not a:return False
    salt=base64.b64decode(a["salt"]);expected=base64.b64decode(a["hash"])
    return secrets.compare_digest(hashlib.pbkdf2_hmac("sha256",password.encode(),salt,ITER),expected)
if __name__=="__main__":
    if len(sys.argv)>=3 and sys.argv[1]=="add":add(sys.argv[2],getpass.getpass("Password: "));print("Account created")
    elif len(sys.argv)>=3 and sys.argv[1]=="check":print("OK" if check(sys.argv[2],getpass.getpass("Password: ")) else "DENIED")
    else:print("Usage: account-manager.py add USERNAME | check USERNAME")
