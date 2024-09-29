from app import app
from model.user_model import user_model
obj= user_model()

@app.route("/user/signup")
def user_signup_contoller():
    #return "This is SignUp Operation"
    return obj.user_signup_model()
