from db_structure import get_con, close_con
con,cur=get_con()
for i in range(100):
	cur.execute("insert into customer values({0}, 'name{0}', 'information{0}')".format(i))
con.commit()
close_con(con,cur)