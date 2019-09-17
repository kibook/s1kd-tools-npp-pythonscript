import os
import subprocess
import Npp

def main():
	scriptdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

	CREATE_NO_WINDOW=0x08000000

        cwd = os.getcwd()
        os.chdir(scriptdir + "\\bin")

        args = [
                "s1kd-appcheck.exe",
                "-v"]

	p = subprocess.Popen(
		args,
		shell=True,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
                env={"XML_CATALOG_FILES": os.environ["XML_CATALOG_FILES"]},
		creationflags=CREATE_NO_WINDOW)
		
	(out, err) = p.communicate(Npp.editor.getText())
	e = p.wait()

	if e == 0:
		Npp.notepad.messageBox(err)
        else:
                Npp.notepad.new()
                Npp.editor.setText(err)

        os.chdir(cwd)

main()
