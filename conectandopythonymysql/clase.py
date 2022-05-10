import mysql.connector

# mydb = mysql.connector.connect(
#     host="35.239.201.186",
#     user="delfosmc",
#     password="analiticadelfos-mc"
# )

# mycursor = mydb.cursor()
# mycursor.execute("create database delfosmasterclassdatabase")
# mycursor.execute("show databases")

# for i in mycursor:
#     print(i)

########

mydb = mysql.connector.connect(
    # host="35.239.201.186",
    # user="delfosmc",
    # password="analiticadelfos-mc",
    # database="delfosmasterclassdatabase"
    # Usar tus propias claves
)

mycursor = mydb.cursor()
# mycursor.execute("create table cliente (id int auto_increment primary key, nombre varchar(255), edad int, direccion varchar(255))")
mycursor.execute("show tables")

for x in mycursor:
    print(x)


########

# sql = "insert into cliente (nombre, edad, direccion) values ('Alberto Herrera López', 28, 'Morelia, Mich')"
# sql = "insert into cliente (nombre, edad, direccion) values (%s, %s, %s)"
# val = ("Antonio Banderas", 50, "Miami")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount)


#########

# sql = "select * from cliente"
# mycursor.execute(sql)

# # result = mycursor.fetchall()
# result = mycursor.fetchone()
# for r in result:
#     print(r)

########

# sql = "insert into cliente (nombre, edad, direccion) values(%s, %s, %s)"
# val = [
#     ("Jonh Ross", 29, "Siempre viva"),
#     ("John Dwayne", 43, "América num 2"),
#     ("Juan Pérez", 23, "Guatemala"),
#     ("Juan Jonhson", 23, "Guatemala"),
# ]

# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount)


#########

# sql = "select * from cliente where direccion = 'Guatemala'"
# mycursor.execute(sql)
# result = mycursor.fetchall()

# for x in result:
#     print(x)

##########

# sql = "update cliente set nombre = '{0}' where nombre = 'Juan Pérez'"
# mycursor.execute(sql.format("Juan Pérez Pérez"))
# mydb.commit()
# print(mycursor.rowcount)

##########

# sql = "delete from cliente where direccion = 'Guatemala'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount)


##########

# sql = "drop table cliente"
# mycursor.execute(sql)

