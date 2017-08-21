import logging
import socket
logging.basicConfig(level=logging.INFO)
#port=443
#port=80
port=4040
host='www.google.com'
try:
	s=socket.socket()
	s.connect((host, port))
	logging.info("connected")
except Exception as err:
	
	logging.exception(err)
