# function_test_!.py
import sys;

# args = sys.argv[1:];

# print  args[0]
# n = int(args[0]);

def test (n):
	if n == 0 : return 0;
	if n ==1 : return 1;
	
	return test(n-2) + test(n-1);

for i in range(10):
	print (test(i));

# result = test (n);
# print result;

