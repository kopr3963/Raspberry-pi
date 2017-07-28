#File_read.py
#_*_coding: utf-8-*-


file = open('newFile.txt','r');

while True:
	line = file.readline();
	if not line : break
	print (line)



file.close();


