from pynput.keyboard import Key, Controller
import time
import urllib.request

keyboard = Controller()

f = urllib.request.urlopen("https://gist.githubusercontent.com/Hemzyy/581b034b7330bb2150a636e8c7eae370/raw/90aa78564df9760490da85d2a310f95c7ddf4554/shrekscript.txt")
script = f.read()

scriptLines = script.decode().split('\n\n')

lines = []
for line in scriptLines:
	lines.append(line)

time.sleep(4)

for line in lines:
	for char in line:
		keyboard.press(char)
		keyboard.release(char)
		time.sleep(0.04)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	time.sleep(0.3)
