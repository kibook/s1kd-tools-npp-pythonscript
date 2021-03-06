import os
import subprocess
import Npp

def main():
	scriptdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	s1kd_refs = scriptdir + "\\bin\\s1kd-refs.exe"

	CREATE_NO_WINDOW=0x08000000

        cwd = os.getcwd()

	try:
		os.chdir(os.path.dirname(Npp.notepad.getCurrentFilename()))
	except:
		pass

	args = [s1kd_refs, "-U"]

	p = subprocess.Popen(
		args,
		shell=True,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		creationflags=CREATE_NO_WINDOW)
		
	(out, err) = p.communicate(Npp.editor.getText())
	e = p.wait()

        if e != 0:
            Npp.notepad.messageBox(err)

        Npp.editor.setText(out)

        os.chdir(cwd)
	
main()
