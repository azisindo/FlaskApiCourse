import pymysql
import json
from flask import make_response
from  datetime import datetime,timedelta
import jwt

class user_model():
    def __init__(self):

        timeout = 50
        self.connection=pymysql.Connect(
                       ada di folder python
                       )

        try:
            self.cursor = self.connection.cursor()
            self.connection.autocommit=True
            print("konek")
        except:
            print("gagal") 

    def user_getall_model(self):
        #business logic
         self.cursor.execute("select * from users")
         result = self.cursor.fetchall()
         if len(result)>0:
             return make_response({"payload":result},200)
         else:
             
             #print (result)
             return make_response({"mesage":"no data found"},204)


        #  if len(result)>0:
        #      return json.dumps(result)
        #  else:
             
        #      #print (result)
        #      return "no data found"
    def user_addone_model(self,data):
        self.cursor.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES ('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        self.connection.commit()
        return make_response({"message":"suces fully this is user_addone_model"},201)
    
    def user_update_model(self,data):
        self.cursor.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id ='{data['id']}' ")
        self.connection.commit()

        if self.cursor.rowcount> 0:
            return make_response({"message":"User Updated Succesfully"},201)
        else:
            return make_response({"message":"Nothing Updated"},204)
        
    def user_delete_model(self,id):
        self.cursor.execute(f"DELETE FROM  users  WHERE id ={id} ")
        self.connection.commit()

        if self.cursor.rowcount> 0:
            return make_response({"message":"User Deleted Succesfully"},200)
        else:
            return make_response({"message":"Nothing delete new"},202)
        
    def user_patch_model(self,data,id):
        
        qry="UPDATE users SET "

        for key in data:
            qry += f"{key}='{data[key]}',"

        qry = qry[:-1] + f" WHERE id={id}"    

        self.cursor.execute(qry)
        self.connection.commit()

        if self.cursor.rowcount> 0:
            return make_response({"message":"User Updated PATCH Succesfully"},201)
        else:
            return make_response({"message":"Nothing Updated PATCH"},204)
        
    def user_pagination_model(self,limit,page):
        limit=int(limit)
        page=int(page)
        start=(page*limit)-limit
        qry=f"SELECT * FROM users LIMIT {start},{limit} "
        self.cursor.execute(qry)
        result = self.cursor.fetchall()
        self.connection.close()
        if len(result) > 0 :
            res = make_response({"payload":result,"page_no":page,"limit":limit},200)
            res.headers['Access-Control-Allow-Origin'] = "*"
            return res
        else:
            return make_response({"message":"No Data Found"},204)
    def user_upload_avatar_model(self,uid,filepath):
        self.cursor.execute(f"UPDATE users SET avatar = '{filepath}' WHERE id='{uid}' ")
        self.connection.commit()

        if self.cursor.rowcount> 0:
            return make_response({"message":"User Updated PATCH Succesfully"},201)
        else:
            return make_response({"message":"Nothing Updated PATCH"},204)

    def user_login_model(self,data):
        self.cursor.execute(f"SELECT id, name , email, phone , avatar , role_id FROM users WHERE email = '{data['email']}' and password='{data['password']}' ")
        result=self.cursor.fetchall()
        userdata = result[0]
        exp_time = datetime.now() + timedelta(minutes=15)
        exp_epoch_time =int(exp_time.timestamp())
        payload = {
                    "payload":userdata,
                    "exp":exp_epoch_time
                   }
        jwtkn=jwt.encode(payload,"screet",algorithm="HS256")
        return make_response({"token":jwtkn},200)
    
    def user_add_multiple_model(self,data):
        qry = "INSERT INTO users (name,email,phone,role_id)  VALUES "
        for userdata in data:
            qry +=f"('{userdata['name']}','{userdata['email']}','{userdata['phone']}','{userdata['role_id']}'),"

        finalqry= qry.rstrip(",")

        self.cursor.execute(finalqry)
        self.connection.commit()

        if self.cursor.rowcount> 0:
            return make_response({"message":"User add Succesfully"},201)
        else:
            return make_response({"message":"Nothing add "},204)