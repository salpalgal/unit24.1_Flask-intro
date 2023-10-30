from flask import Flask


app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "Welcome!"

@app.route("/welcome/home")
def welcomeHome():
    return "Welcome home!"

@app.route("/welcome/back")
def welcomeBack():
    return "Welcome back!"



if __name__ == "__main__":
    app.run(FLASK_ENV="environement")
    