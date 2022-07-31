const {ipcRenderer} = require("electron");
var FilerCli = [];

function IsEnter()
{
	const input = document.getElementById("Seed");
	if (input.value != "")
	{
		if (event.keyCode == 13) ChooseSeed();
	}
}

function SelectFile()
{
    var Filename = document.getElementById("OpenFile");
    var Label = document.getElementById("Selector");

	Label.textContent = Filename.files[0].name;
	FilerCli.push(Filename.files[0].path);

	// Hide ChooseFile
	var ChooseFileDiv = document.getElementById("ChooseFile");
	ChooseFileDiv.classList.toggle("fade");
	ChooseFileDiv.style.visibility = "hidden";

	// Show Seed input field
	var SeedDiv = document.getElementById("SeedDiv");
	SeedDiv.classList.toggle("fade");
	SeedDiv.style.visibility = "visible";
}

function ChooseSeed()
{
	var SeedDiv = document.getElementById("Seed");
	FilerCli.push(`-s ${SeedDiv.value}`);

	// Hide Seed input field
	SeedDiv.classList.toggle("fade");
	SeedDiv.style.visibility = "hidden";

	// Show encrypt decrypt buttons
	var ModeDiv = document.getElementById("Mode");
	ModeDiv.classList.toggle("fade");
	ModeDiv.style.visibility = "visible";
}

function Encrypt()
{
	ipcRenderer.send("args", `-e "${FilerCli[0]}" ${FilerCli[1]}`);

	// Hide encrypt decrypt buttons
	var ModeDiv = document.getElementById("Mode");
	ModeDiv.classList.toggle("fade");
	ModeDiv.style.visibility = "hidden";

	// Show ThankYou message
	var ModeDiv = document.getElementById("ThanksGiving");
	ModeDiv.classList.toggle("fade");
	ModeDiv.style.visibility = "visible";
}

function Decrypt()
{
	ipcRenderer.send("args", `-d "${FilerCli[0]}" ${FilerCli[1]}`)

	// Hide encrypt decrypt buttons
	var ModeDiv = document.getElementById("Mode");
	ModeDiv.classList.toggle("fade");
	ModeDiv.style.visibility = "hidden";

	// Show ThankYou message
	var ModeDiv = document.getElementById("ThanksGiving");
	ModeDiv.classList.toggle("fade");
	ModeDiv.style.visibility = "visible";
}
