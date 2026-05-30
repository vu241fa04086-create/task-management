from flask import Flask, render_template
from flasgger import Swagger

from config.database import init_db
from config.oauth_config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET
from routes.ai_routes import ai_bp
from routes.auth_routes import auth_bp
from routes.map_routes import map_bp
from routes.oauth_routes import init_oauth, oauth_bp
from routes.payment_routes import payment_bp
from routes.task_routes import task_bp

app = Flask(__name__)

# 1. App Configuration
app.config["SECRET_KEY"] = "supersecretkey"  # Used for sessions and OAuth
app.config["GOOGLE_CLIENT_ID"] = GOOGLE_CLIENT_ID
app.config["GOOGLE_CLIENT_SECRET"] = GOOGLE_CLIENT_SECRET

# Swagger UI configuration
app.config["SWAGGER"] = {
    "title": "Task Management",
    "uiversion": 3
}

# 2. Initialize Extension Templates
swagger_template = {
    "swagger": "2.0",
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    }
}

# Initialize Swagger ONCE after configurations are set
swagger = Swagger(app, template=swagger_template)

# 3. Initialize Databases and Services
init_db(app)
init_oauth(app)

# 4. Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(oauth_bp, url_prefix="/auth")
app.register_blueprint(task_bp, url_prefix="/api/tasks")
app.register_blueprint(payment_bp, url_prefix="/api/payment")
app.register_blueprint(map_bp, url_prefix="/map")
app.register_blueprint(ai_bp, url_prefix="/api/ai")

# 5. Routes
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )