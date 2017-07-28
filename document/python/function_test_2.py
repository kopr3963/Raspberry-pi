# function_test_2.py
#_*_coding: utf-8-*-

file = open('file.txt','r');
lines = file.readlines();
total = 0;
avg = 0;
for a in lines :
	total = total +  int(a);
print '총합 : ',total
avg = total / len(lines);
print '평균 : ',avg

file.close();
f = open ('result.txt','w');
f.write('%d'% avg);
f.close();

