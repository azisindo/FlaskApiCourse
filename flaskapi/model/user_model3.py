import pymysql
import json

class user_model():
    def __init__(self):

        timeout = 50
        self.connection=pymysql.Connect(charset="utf8mb4",
                        connect_timeout=timeout,
                        cursorclass=pymysql.cursors.DictCursor,
                        write_timeout=timeout,
                        )

        try:
            self.cursor = self.connection.cursor()
            self.connection.autocommit=True
            print("konek")
        except:
            print("gagal") 

    def user_getall_model(self):
        #business logic
         self.cursor.execute("select * from users where id=100")
         result = self.cursor.fetchall()
         if len(result)>0:
             return json.dumps(result)
         else:
             
             #print (result)
             return "no data found"
    def user_addone_model(self,data):
        self.cursor.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES ('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        self.connection.commit()
        return "suces fully this is user_addone_model"
    
    def user_update_model(self,data):
        self.cursor.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id ='{data['id']}' ")
        self.connection.commit()

        if self.cursor.rowcount> 0:
            return "User Updated Succesfully"
        else:
            return "Nothing Updated"
        
    def user_delete_model(self,id):
        self.cursor.execute(f"DELETE FROM  users  WHERE id ={id} ")
        self.connection.commit()

        if self.cursor.rowcount> 0:
            return "User Deleted Succesfully"
        else:
            return "Nothing delete new"        