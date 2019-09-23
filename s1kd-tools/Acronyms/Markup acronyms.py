import os
import subprocess
import Npp

def main():
	scriptdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	s1kd_acronyms = scriptdir + "\\bin\\s1kd-acronyms.exe"

	CREATE_NO_WINDOW=0x08000000

        filedir = os.path.dirname(Npp.notepad.getCurrentFilename())
        cwd = os.getcwd()

	try:
		os.chdir(filedir)
	except:
		pass

	args = [s1kd_acronyms, "-m"]

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
		Npp.editor.setText(out)
	else:
		Npp.notepad.messageBox(err)

        os.chdir(cwd)

main()
