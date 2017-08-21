from db_structure import get_con, close_con
def get_data(c_id=None):
	q="select * from customer"
	if c_id:
		q=q+" where id=%s"%c_id
	con,cur = get_con()
	cur.execute(q)
	data=cur.fetchall()
	close_con(con,cur)
	return data
if __name__ == "__main__":
	print get_data()