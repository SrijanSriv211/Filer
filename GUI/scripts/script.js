function GetFileName()
{
    var exec = require("child_process");
    var FileInput = document.getElementById("OpenFile");

    exec.exec("start .", function (err, stdout, stderr) {
        if (err)
        {
            console.error(err);
            return;
        }

        console.log(stdout);
    });
}
