import unittest
from db_structure import get_config, get_con
class Test_db_structure(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print "login"
		cls.user="user instance "
	@classmethod
	def tearDownClass(cls):
		print "logout from app"
		cls.user=None
	def setUp(self):
		print "setup"
		print self.user
	def tearDown(self):
		print "teardown"

	def test_test1(self):
		print "test1"
		exp= ['host', 'db', 'pwd', 'user']
		data = get_config()
		act=data.keys()
		error = "exp: %s, Got: %s"%(exp, act)
		self.assertTrue(exp==act,error)

	def test_test2(self):
		print "test2"
		exp= ['host', 'db', 'pwd']
		data = get_config()
		act=data.keys()
		error = "exp: %s, Got: %s"%(exp, act)
		self.assertFalse(exp==act,error)
	


#unittest.main()
