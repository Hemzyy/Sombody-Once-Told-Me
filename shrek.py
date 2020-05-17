from pynput.keyboard import Key, Controller
import time
import urllib.request

keyboard = Controller()

f = urllib.request.urlopen("https://gist.githubusercontent.com/Hemzyy/581b034b7330bb2150a636e8c7eae370/raw/f482a9aaebb994078000e12574b79a4aa006f8c8/shrekscript.txt")
script = f.read()

scriptLines = script.decode().split('\n\n')

lines = []
for line in scriptLines:
	lines.append(line)

print('You have 4 seconds to click in a textBox')
time.sleep(4)

for line in lines:
	for char in line:
		keyboard.press(char)
		keyboard.release(char)
		time.sleep(0.04)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	time.sleep(0.3)
