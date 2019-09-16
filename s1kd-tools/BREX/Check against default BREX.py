import subprocess
import os
import Npp

def main():
	scriptdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	s1kd_brexcheck = scriptdir + "\\bin\\s1kd-brexcheck.exe"

	CREATE_NO_WINDOW=0x08000000

	args = [s1kd_brexcheck, "-B", "-c", "-v"]

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

main()
