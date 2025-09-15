from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from backend.models import db, User
from backend.config import Config

# Initialize Flask
app = Flask(__name__)
app.config.from_object(Config)

# Extensions
bcrypt = Bcrypt(app)
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register routes
from backend.routes.auth_routes import auth_bp
from backend.routes.mood_routes import mood_bp
from backend.routes.dashboard_routes import dashboard_bp

app.register_blueprint(auth_bp)
app.register_blueprint(mood_bp)
app.register_blueprint(dashboard_bp)

@app.route('/')
def home():
    return "Mental Health Mood Tracker is running with SQL!"

# Create tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
