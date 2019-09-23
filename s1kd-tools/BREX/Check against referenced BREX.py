import subprocess
import os
import Npp
import ConfigParser

def main():
	scriptdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	s1kd_brexcheck = scriptdir + "\\bin\\s1kd-brexcheck.exe"

	CREATE_NO_WINDOW=0x08000000

        filedir = os.path.dirname(Npp.notepad.getCurrentFilename())
        cwd = os.getcwd()

        try:
            os.chdir(filedir)
        except:
            pass

	args = [s1kd_brexcheck, "-v"]

        config = ConfigParser.RawConfigParser()
        config.read(scriptdir + "\\settings.ini")

        if config.get("BREX", "CheckValues") == "yes":
            args.append("-c")

        if config.get("BREX", "Layered") == "yes":
            args.append("-l")

	p = subprocess.Popen(
		args,
		shell=True,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
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
