import socket
import typer
import os
import PyXML.xmlparse
from werkzeug.utils import secure_filename
xml = PyXML.xmlparse

app = typer.Typer()

@app.command(name="import")
def _import(mirrorpath):
    if os.path.exists(mirrorpath):
        print("Importing %s..." % mirrorpath)
        code = open(mirrorpath).read()
        url = xml.ParseXMLElement(code,"URL")
        print("Using Adress %s..." % url)
        with open("package.xml", "w") as f:
            f.write(code)

@app.command()
def clone(file):
    print("UNFS Loading Websocket...")
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("UNFS Parsing `package.xml`")
    code = open("package.xml", "r").read()
    url = xml.ParseXMLElement(code,"URL")
    IPAddr = socket.gethostbyname(url)
    print(f"UNFS Connecting to {IPAddr}...")

    sc.connect((IPAddr, 4443))
    print(f"UNFS Receiving Data...")
    sc.send(f"clone@{file}".encode())
    f = sc.recv(10000)
    print(f"Writing file: {file}")
    with open(os.getcwd()+"/"+secure_filename(file),"wb") as fp:
        fp.write(f)
    sc.close()
    
app()