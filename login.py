import sqlite3

from flask import request, redirect, render_template, Blueprint
from werkzeug.security import check_password_hash

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password, role FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        if user and check_password_hash(user[0], password):
            role = user[1]
            if role == 'admin':
                return redirect('/admin')
            else:
                return redirect('/user')
        return "Invalid credentials"
    return render_template('login.html')
