const {app, BrowserWindow, ipcMain} = require("electron");
const child_process = require('child_process');

function Exec(command)
{
	var child = child_process.exec
	child(command, function (err, stdout, stderr) {
		if (err)
		{
			console.error(err);
			return;
		}

		console.log(stdout);
		// process.exit();
	});
}

function CreateWindow()
{
	const Display = new BrowserWindow({
		title: "Filer", icon: "../Logo.ico",
		width: 400, height: 650, maximizable: false,
		webPreferences: {
			nodeIntegration: true,
			contextIsolation: false
		}});

	Display.menuBarVisible = false;
    Display.loadFile("index.html");
    // Display.webContents.openDevTools();
}

app.whenReady().then(CreateWindow);

// Quit when all windows are closed.
app.on('window-all-closed', () => {
	// On OS X it is common for applications and their menu bar
	// to stay active until the user quits explicitly with Cmd + Q
	if (process.platform !== 'darwin')
	{
		app.quit();
	}
});
  
app.on('activate', () => {
	// On OS X it's common to re-create a window in the app when the
	// dock icon is clicked and there are no other windows open.
	if (BrowserWindow.getAllWindows().length === 0)
	{
		CreateWindow();
	}
});

ipcMain.on("args", (event, arg) => {
	// console.log(`python ..\\filer_cli.py ${arg}`);
	Exec(`python ..\\filer_cli.py ${arg}`);
});
