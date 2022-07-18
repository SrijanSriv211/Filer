const {app, BrowserWindow} = require("electron");

function CreateWindow()
{
    const Display = new BrowserWindow({ width: 400, height: 650 });
    Display.loadFile("index.html");
}

app.whenReady().then(CreateWindow);
