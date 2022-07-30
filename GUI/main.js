const {app, BrowserWindow} = require("electron");

function CreateWindow()
{
    const Display = new BrowserWindow({ title: "Filer", icon: "../Logo.ico", width: 400, height: 650, maximizable: false });
    Display.menuBarVisible = false;
    Display.loadFile("index.html");
}

app.whenReady().then(CreateWindow);
