#class_first.py
#_*_coding: utf-8-*-
class Calculator:

	count = 0;
	def __init__ (self):
		self.result =0;
		print('Calculator()');
		print ('self :: ' , self);
		print type(self)
	secret = "secret";
	def test(self,num) :
		return num

cal1 = Calculator();
cal2 = Calculator();
print cal1.test(3);

cal2 = cal1;

print cal1 is cal2
print cal1.secret;

print type(cal1)



#