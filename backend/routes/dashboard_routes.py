from flask import Blueprint, render_template
from flask_login import login_required, current_user
from backend.models import Mood

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    moods = Mood.query.filter_by(user_id=current_user.id).order_by(Mood.date.desc()).all()
    return render_template('dashboard.html', moods=moods)
