from flask import Flask
app = Flask(__name__)

@app.route("/")

def home():
    return "Hi"


@app.route("/test_login")
def auth(name, pw):
    if name == "name" and pw == "pass":
        return "Authenticated"
    else:
        return "Wrong password"