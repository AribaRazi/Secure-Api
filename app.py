from flask import Flask
from flask_jwt_extended import JWTManager
from routes.auth import auth_bp
from routes.quotes import quotes_bp
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET")  

jwt = JWTManager(app)

@app.route("/home")
def home():
    return "hey! your flask app is running"

app.register_blueprint(auth_bp)
app.register_blueprint(quotes_bp)

if __name__ == "__main__":
    app.run(debug=True)
