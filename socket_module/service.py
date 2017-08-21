import socket
from db_operation import get_data
try:
	s=socket.socket()
	#host="tcloudost-VirtualBox"
	host=socket.gethostname()
	port=8889
	s.bind((host,port))
	s.listen(5)
	print "waiting for the client request"
	co, ci =  s.accept()
	co.send("got the connection")
	c_id=co.recv(1024)
	print "got the customer id:%s"%c_id
	data = get_data(c_id)
	print "data filtered:%s"%data
	co.send(str(data))
except Exception as err:
	print err
finally:
	s.close()
