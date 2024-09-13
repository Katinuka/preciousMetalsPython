from flask import request, redirect, render_template, Blueprint
from werkzeug.security import generate_password_hash
import sqlite3

registration_bp = Blueprint('registration', __name__)


def add_user(username, password):
    hashed_password = generate_password_hash(password)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, 'user')", (username, hashed_password))
    conn.commit()
    conn.close()


@registration_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        add_user(username, password)
        return redirect('/login')
    return render_template('register.html')
