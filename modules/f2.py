
def fun():
	print "This is fun in f2 in modules"
def main():
	print "this is f1"
	print "__name__",__name__
	fun()

if __name__ == "__main__":
	main()
