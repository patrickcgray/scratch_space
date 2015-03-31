'''
Created on July, 16 2014

@author: pgray
'''

#install tkinter
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

filename = filedialog.askopenfilename(parent=root,title='Open file to scrub')

original_file = open(filename, "r")
lines = original_file.readlines()
original_file.close()

#todo it will break if there are any other periods...
intermediate_filename, extension = filename.split(".")
new_filename = intermediate_filename + "_scrubbed." + extension 
new_file = open(new_filename, "w")
new_lines = []

dead_signal  = False
for index, value in enumerate(lines):
	if dead_signal:
		dead_signal = False
		continue
	if value[0:7] == "<signal":
		if lines[index+1][0:9] == "</signal>":
			dead_signal = True
			continue
	new_file.write(str(value))

new_file.close()