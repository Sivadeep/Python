'''
import f1
f1.fun()
'''
'''
import f1 as file1
file1.fun()
'''
'''
from f1 import fun
fun()
'''
'''
import f1
f1.fun()
'''
'''
import f2
f2.main()
f2.fun()
'''
'''
import f1
import f2
f1.fun()
f2.fun()
'''
'''
from f1 import fun
from f2 import fun
def fun():
	print "this fun in app1"
fun()
'''
'''
import sqlite3
import sys
#sys.path.append('/home/tcloudost/Desktop')
sys.path.insert(0,'/home/tcloudost/Desktop')
print sys.path
import f2
f2.fun()
'''
'''
import module1
module1.file1.fun()
module1.file2.fun()
'''
from module1 import file1, file2
file1.fun()
file2.fun()




















