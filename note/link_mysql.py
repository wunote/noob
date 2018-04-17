# conding:uft-8

import MySQLdb

db = MySQLdb.connect(
        host = 'localhost',
        port = 3306,
        user = "root",
        passwd = "fisCw##84^%37Lorms",
        db = "test"
        )

cur = db.cursor()

#cur.execute("delete from student where name='Word'")
#cur.execute("insert into student values ('Tan',23)")
#cur.execute("update student set name='Sun' where name='Tom'")
#db.commit()
cur.execute("select * from student")
for i in cur.fetchall():
    print "name:",i[0],"age:",i[1]

#print cur.fetchall()

#try:
#    result = cur.execute("insert into student (name,age) VALUES ('helloword',24)")
#    db.commit()
#    print result
#except Exception as e:
#    db.follback()

cur.close()
db.close()
