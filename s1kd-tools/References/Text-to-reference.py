import os
import subprocess
import Npp
import ConfigParser

def main():
	scriptdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	s1kd_ref = scriptdir + "\\bin\\s1kd-ref.exe"

	CREATE_NO_WINDOW=0x08000000

	config = ConfigParser.RawConfigParser()
	config.read(scriptdir + "\\settings.ini")

	args = [s1kd_ref]

	if config.get("References", "GuessPrefix") == "yes":
		args.append("-g")

	text = Npp.editor.getSelText()

	hasSelectedText = text != ''

	if not hasSelectedText:
		args.append(["-T", "all"])
		text = Npp.editor.getText()

	p = subprocess.Popen(
		args,
		shell=True,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		creationflags=CREATE_NO_WINDOW)

	(out, err) = p.communicate(text)
	e = p.wait()
	if err == 0:
		if hasSelectedText:
			Npp.editor.replaceSel(out)
		else:
			Npp.editor.setText(out)
	else:
		Npp.notepad.messageBox(err, "s1kd-ref")

main()
