import os
import subprocess
import Npp

def main():
	scriptdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	s1kd_ref = scriptdir + "\\bin\\s1kd-ref.exe"

	CREATE_NO_WINDOW=0x08000000

	buf = Npp.notepad.getCurrentBufferID()

	Npp.notepad.menuCommand(MENUCOMMAND.FILE_OPEN)

	if Npp.notepad.getCurrentBufferID() == buf:
		return

	path = Npp.notepad.getCurrentFilename()

	Npp.notepad.close()
	Npp.notepad.activateBufferID(buf)

	args = [s1kd_ref, "-d", "-i", "-l", "-t", path]

	p = subprocess.Popen(
		args,
		shell=True,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		creationflags=CREATE_NO_WINDOW)
		
	(out, err) = p.communicate()
	e = p.wait()

	Npp.editor.addText(out)
	
main()