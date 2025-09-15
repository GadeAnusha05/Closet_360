from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_required, current_user
from backend.models import db, Mood
from textblob import TextBlob

mood_bp = Blueprint('mood', __name__)

@mood_bp.route('/log_mood', methods=['POST'])
@login_required
def log_mood():
    journal = request.form['journal']
    sentiment = TextBlob(journal).sentiment.polarity
    mood = 'Happy' if sentiment > 0 else 'Sad' if sentiment < 0 else 'Neutral'

    new_mood = Mood(journal=journal, sentiment=sentiment, mood=mood, user_id=current_user.id)
    db.session.add(new_mood)
    db.session.commit()

    flash('Mood logged successfully!', 'success')
    return redirect(url_for('dashboard.dashboard'))
