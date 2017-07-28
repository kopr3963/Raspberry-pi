# File_Read_List.py
#_*_coding: utf-8-*-

file = open('newFile.txt','r');
lines = file.readlines();

print  "readlines()는 리스트형태로 가지고옴." + lines[0] 
for line in lines :
	print line
file.close()