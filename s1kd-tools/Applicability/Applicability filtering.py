import os
import subprocess
import Npp
import sys

def main():
	scriptdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	s1kd_instance = scriptdir + "\\bin\\s1kd-instance.exe"

	CREATE_NO_WINDOW=0x08000000

        filters = Npp.notepad.prompt("Enter a comma-separated list of assignments, in the form of <ident>:<type>=<value>. For example: version:prodattr=A,weather:condition=icy", "Applicability filtering", "")

	if filters == None:
		return

	args = [s1kd_instance, "-y"]

        for f in filters.split(","):
            args.append("-s")
            args.append(f)

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
		Npp.notepad.new()
		Npp.editor.setText(out)
	else:
		Npp.notepad.messageBox(err)

main()
