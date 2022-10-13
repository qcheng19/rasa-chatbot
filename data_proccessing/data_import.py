# import sqlite3
# con = sqlite3.connect('rasa.db')

# def sql_table(con):
#     cursorObj = con.cursor() 
#     cursorObj.execute("CREATE TABLE user(name text PRIMARY KEY, phoneNumber text)")
#     cursorObj.execute("CREATE TABLE vehicle(vehicleName text PRIMARY KEY, usage INTEGER, vehicleStatus text, vehiclePosition text)")
#     # sql="DROP TABLE vehicle"
#     # cursorObj.execute(sql)
    
#     con.commit()
# sql_table(con)



# # cursorObj = con.cursor()   
# # cursorObj.execute('INSERT INTO user(name) VALUES(?)', ("hhh",))   
# # con.commit()

# # def sql_fetch(con):
# #     cursorObj = con.cursor()
# #     back_name = cursorObj.execute('SELECT name FROM user WHERE name = ?', ("hhh",))


# #     print(back_name.fetchone()[0])
# #     # if vehicle_name == back_name:
# #     #     return True
# #     # else:
# #     #     return False
# # sql_fetch(con)

# # def insert_name(con,name):
# #     cursorObj = con.cursor()
# #     cursorObj.execute('INSERT INTO user(name) VALUES(?)', (name,))   
# #     con.commit()
# # name="chengqihAO"
# # insert_name(con, name)

# # 删除空用户名
# # def sql_update(con):
# #     cursorObj = con.cursor()
# #     # sql = "UPDATE user SET name = ? where name = h111111"
# #     # sql = "DELETE from vehicle WHERE vehicleName is null"
# #     sql = "DELETE from vehicle WHERE usage = 1"
# #     cursorObj.execute(sql)
# #     con.commit()
# # sql_update(con)

# # def fetch_all_car(con):
# #     cursorObj = con.cursor()
# #     cursorObj.execute("SELECT vehicleName FROM vehicle WHERE usage = 1")
# #     back_name = cursorObj.fetchall()
# #     print(back_name)
# #     s = ""
# #     for row in back_name:
# #         s = s + row[0] + "\n"
# #     print(s)
# # fetch_all_car(con)
# # def sql_fetch(con, sql_name, name):
# #     cursorObj = con.cursor()
# #     cursorObj.execute('SELECT name FROM user')
# #     back_name = cursorObj.fetchall()[0]
# #     print(back_name)
# #     if name in back_name:
# #         print(name)
# #         return True
# #     else:
# #         print('g')
# #         return False
# # sql_name="user"
# # name="mack"
# # sql_fetch(con, sql_name, name)

# # def sql_fetch_user(con, name):
# #     cursorObj = con.cursor()
# #     cursorObj.execute('SELECT name FROM user')
# #     # back_name = cursorObj.fetchall()
# #     for back_name in cursorObj.fetchall():
# #         if back_name[0] == name:
# #             return True
# #     return False

# # def sql_update(con,car_name, line_name, value):
# #     cursorObj = con.cursor()
# #     if(line_name == 'vehicleStatus'):
# #         sql = "UPDATE vehicle SET vehicleStatus=? where vehicleName = ?"
# #     elif line_name == 'usage':
# #         sql = "UPDATE vehicle SET usage=? where vehicleName = ?"
# #     else:
# #         sql = "UPDATE vehicle SET vehiclePosition=? where vehicleName = ?"
# #     cursorObj.execute(sql,(value, car_name,))
# #     con.commit()

# # sql_update(con, "h2222", "usage", "1")


# # def insert_name(con,name):
# #     cursorObj = con.cursor()
# #     # cursorObj.execute('INSERT INTO vehicle(vehicleName) VALUES(?)', (name,))   

# #     sql = "UPDATE vehicle SET usage=?"
# #     cursorObj.execute(sql,(1,))
# #     con.commit()

# # name='Lamborghini'
# # insert_name(con, name)