from flask import Blueprint, render_template, session
from functools import wraps

main_bp = Blueprint('main', __name__)

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user' not in session:
            return render_template('auth/login.html')
        return f(*args, **kwargs)
    return decorated

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/dashboard')
@requires_auth
def dashboard():
    return render_template('dashboard.html', user=session['user'])
