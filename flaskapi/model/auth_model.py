import pymysql
import json
from flask import make_response,request
from  datetime import datetime,timedelta
import jwt
import re
from functools import wraps

class auth_model():
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

    def token_auth(self,endpoint=""):
        def inner1(func):
            @wraps(func)
            def inner2(*args):
                endpoint = request.url_rule
                print(endpoint)
                print(request.headers.get("Authorization"))  
                authorization = request.headers.get("Authorization")
                if re.match("^Bearer *([^ ]+) *$",authorization,flags=0):
                    #split_auth=authorization.split(".")
                    token = authorization.split(" ")[1]
                    # print(token)
                    # print(jwt.decode(token,"screet",algorithms="HS256"))
                    try:
                        jwtdecoded = jwt.decode(token,"screet",algorithms="HS256")
                    except jwt.ExpiredSignatureError:
                        return make_response({"ERROR":"TOKEN_EXPIRED"},401)    

                    role_id =  jwtdecoded['payload']['role_id']
                    print(jwtdecoded)
                    print(role_id)
                    self.cursor.execute(f"SELECT roles FROM accessbility_view WHERE endpoint = '{endpoint}'")
                    result = self.cursor.fetchall()

                    if len(result) > 0 :
                       print(json.loads(result[0]['roles']))
                       allowed_roles = json.loads(result[0]['roles'])
                       if role_id in allowed_roles:
                          return func(*args) 
                       else:
                           return make_response({"ERROR":"INVALID_ROLE"},404)        
                    else:
                        return make_response({"ERROR":"UNKNOW_ENDPOINT"},404)    
                    
                else:
                    return make_response({"ERROR":"INVALID_TOKEN"},401)
            return inner2
        return inner1
