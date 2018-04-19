# coding=UTF8
import os

path = "/Users/akmyrat/desktop/images/"

for filename in os.listdir(path):
	if not filename.startswith('.'):
		print(filename)
		with open(path+filename) as f:
			array = ""
			i = 0
			while i < 5: 	
				c = f.read(1)
				print(c) 
				if c == '}':
					i = i+1
				array = array + c	

			text_file = open("/Users/akmyrat/desktop/converted_images/%s" % filename, "w")
			text_file.write("%s" % array)
			text_file.close()
