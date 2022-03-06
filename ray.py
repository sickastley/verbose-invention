from random import choice as c
import sys

lst = sys.argv
numbers = int(lst[1])

title = ["Alert!", "Danger", "Virus found"]

buttons = [0, 1, 2]
warn = [16, 32]

message = [
"build b1e4c2c9ef4c virus detected. Press OK to start scan.",
"virus escaped from firm ware. initialising trojan removal.",
"could not remove the virus, contact your administrator.",
"virus tried to attack kernel. removal failed successfully.",
"Task failed successfully.",
"sending log to microsoft for secure connection.",
"Reverse shell connected."
]

with open("payload.vbs", "w") as file:
	for a in range(0, numbers):
		file.write(f'''X=MsgBox("{c(message)}", {c(buttons)}+{c(warn)}, "{c(title)}")\n''')