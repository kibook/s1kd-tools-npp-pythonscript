import os
import subprocess
import Npp
import time

def main():
	scriptdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	s1kd_newdml = scriptdir + "\\bin\\s1kd-newdml.exe"

	CREATE_NO_WINDOW=0x08000000

	code = Npp.notepad.prompt("DML code:", "Enter DML code", "")

	if code == None:
		return

	args = [s1kd_newdml, "-#", code, "-@", "-"]

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
