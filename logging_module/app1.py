import logging
logging.basicConfig(level=logging.DEBUG,  
    format="%(asctime)s->%(levelname)s->%(message)s", filename="app1.log")
logging.info("Application started")
a=raw_input("Enter a value:")
b=raw_input("Enter b value:")
logging.debug("a=%s, b=%s"%(a,b))
f=None
try:
    logging.info("opening data1.csv")
    f=open('data1.csv','r')
    data=f.read()
except IOError as err:
    logging.exception("%s"%err)
    logging.exception("file not found")
except Exception as err:
    logging.exception("%s"%err)
    logging.exception("something went wrong.")
finally:
    if f:
        f.close()
        logging.info("File closed sucessfully!!")
logging.info("opening file")
f=open("data6.csv",'w')
try:
    a=int(a)
    b=int(b)
    f.write("%s, %s"%(a,b))
    res=a/b
    f.write(",%s"%res)
except ZeroDivisionError as err:
    logging.exception("%s"%err)
    logging.exception("Dont' enter zero for b value:")
except ValueError as err:
    logging.exception("%s"%err)
    logging.exception("Enter only digits to a,b values.")
    
except Exception as err:
    logging.exception("%s"%err)
    logging.exception("something went wrong")
finally:
    f.close()
    logging.info("File closed successfully")
logging.info("some other statements ")
logging.info("program ended")