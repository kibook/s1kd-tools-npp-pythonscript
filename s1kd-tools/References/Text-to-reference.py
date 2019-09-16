import os
import subprocess
import Npp

def main():
	scriptdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	s1kd_ref = scriptdir + "\\bin\\s1kd-ref.exe"

	CREATE_NO_WINDOW=0x08000000

	args = [s1kd_ref]

	p = subprocess.Popen(
		args,
		shell=True,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		creationflags=CREATE_NO_WINDOW)
		
	(out, err) = p.communicate(Npp.editor.getSelText())
	e = p.wait()

	Npp.editor.replaceSel(out)
	
main()