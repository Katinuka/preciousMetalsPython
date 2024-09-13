from flask import Blueprint

homepages_bp = Blueprint('homepages', __name__)


@homepages_bp.route('/admin')
def admin_home():
    return "<h1>Welcome, Admin!</h1>"


@homepages_bp.route('/user')
def user_home():
    return "<h1>Welcome, User!</h1>"
