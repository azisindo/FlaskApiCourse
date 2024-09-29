from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Bismillah ya allah mudah kan programingnya"

@app.route("/home")
def home():
    return "halaman ke Home"

# import controller.user_controller as user_controller
# import controller.product_controller as product_controller

from controller import product_controller,user_controller

# if __name__=='__main__':
#      app.run(port=5000,debug=True)

