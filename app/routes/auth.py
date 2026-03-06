# app/routes/auth.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from app import db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('tasks.view_tasks'))
        
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):  # In a real application, use hashed passwords and check with check_password_hash
            session['user_id'] = user.id 
            return jsonify({
                'state':'success',
                'message':'Login Successful',
                'redirect':url_for('tasks.view_tasks')})
        else:
            return jsonify({'state':'danger','message':'Invalid username or password'})
    return render_template('login.html')
    

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully!', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('tasks.view_tasks'))
        
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if username and password:
            existing_user = User.query.filter_by(username=username).first()
            if not existing_user:
                hashed_password = generate_password_hash(password)
                new_user = User(username=username, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                return jsonify({
                    'state':'success',
                    'message':'Registration Successful',
                    'redirect':url_for('auth.login')})
            else:
                return jsonify({
                    'state':'info',
                    'message':'User Already Registered',
                    'redirect':url_for('auth.login')})
    return render_template('register.html')
