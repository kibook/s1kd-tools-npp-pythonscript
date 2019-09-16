import os
import subprocess
import Npp
import time

def main():
	scriptdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	s1kd_newdm = scriptdir + "\\bin\\s1kd-newdm.exe"

	CREATE_NO_WINDOW=0x08000000

	dmc = Npp.notepad.prompt("DMC:", "Enter DMC", "")

	if dmc == None:
		return

	args = [s1kd_newdm, "-#", dmc, "-@", "-"]

	p = subprocess.Popen(
		args,
		shell=True,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		creationflags=CREATE_NO_WINDOW)
	
	(out, err) = p.communicate()
	e = p.wait()

	Npp.notepad.new()
	Npp.editor.setText(out)
	
main()