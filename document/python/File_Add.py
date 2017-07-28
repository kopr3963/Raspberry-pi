# File_Add.py
#_*_coding: utf-8-*-


file = open ('newFile.txt','a');

for i in range(11,20):
	data = "%d번째 줄입니다.\n" % i
	file.write(data)
	pass

file.close()
