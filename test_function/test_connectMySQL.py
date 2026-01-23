from connectdb.connectMySQL import connect_mysql

conn = connect_mysql()

if conn:
    print("Kết nối MySQL thành công")
    conn.close()
else:
    print(" Kết nối MySQL thất bại")
