import logging
import socket
logging.basicConfig(level=logging.INFO)
#port=443
#port=80
port=8889
host="tcloudost-VirtualBox"
try:
	s=socket.socket()
	s.connect((host, port))
	ack = s.recv(1024)
	print "ack=",ack
	c_id=raw_input("enter customer id:")
	s.send(c_id)
	resp = s.recv(1024)
	print resp
except Exception as err:
	
	logging.exception(err)
