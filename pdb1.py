import pdb
a=10
b=20
c=a+b
def fun(a1,b1):
	try:
		print "a1=%s, b1=%s"%(a1,b1)
		c1=a1+b1
		return c1
	except Exception as err:
		return 0
print "a=%s,b=%s,c=%s"%(a,b,c)
print "some statements"
res = fun(100,200)
print "result=",res 
pdb.set_trace()
for i in [-3,-4,-5,6,7,0,8,9,3,4,5]:
	if i!=0:
		print 10/i
	else:
		print i
print "program ended"
