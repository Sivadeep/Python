import psycopg2
import logging
logging.basicConfig(filename="installation.txt",level=logging.DEBUG)
def get_config():
	try:
		f=open('config.csv')
		data=f.readlines()
		details = dict([row.split(',') for row in data])
		logging.debug("%s"%details)
		return {key:value.strip('\n') for key,value in details.items()}

	except Exception as err:
		logging.exception(err)


def get_con():
	try:
		config_Data = get_config()
		con = psycopg2.connect(host=config_Data['host'],
			user=config_Data['user'],
			database=config_Data['db'],
			password=config_Data['pwd'])
		cur = con.cursor()
		logging.debug("%s, %s"%(con,cur))
		return con, cur 
	except Exception as err:
		logging.exception(err)

def close_con(con,cur):
	cur.close()
	con.close()

def create_table_customer():
	q="create table customer(id int, name varchar(250),info text)"
	con,cur=get_con()
	cur.execute(q)
	con.commit()
	close_con(con,cur)

def main():
	get_con()
	create_table_customer()

if __name__ == "__main__":
	main()