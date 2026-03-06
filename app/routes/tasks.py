# app/routes/tasks.py

from flask import Blueprint, request, session, render_template, redirect, url_for, flash, jsonify
from app import db
from app.models import Task

task_bp = Blueprint('tasks', __name__)

# API: Get tasks
@task_bp.route('/view')
def view_tasks():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    return render_template('tasks.html')

@task_bp.route('/tasks')
def get_tasks():
    if 'user_id' not in session:
        return jsonify({"state":"danger","message":"Unauthorized"}), 401

    tasks = Task.query.filter_by(user_id=session['user_id']).all()

    task_list = [
        {
            "id": task.id,
            "title": task.title,
            "description":task.description,
            "status": task.status
        }
        for task in tasks
    ]

    return jsonify(task_list)

# API: Add task
@task_bp.route('/add', methods=['POST'])
def add_tasks():
    if 'user_id' not in session:
        return jsonify({"state":"danger","message":"Unauthorized"}), 401

    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if title:
        new_task = Task(
            title=title,
            description=description,
            status='pending',
            user_id=session['user_id']
        )

        db.session.add(new_task)
        db.session.commit()
        return jsonify({
            'state':'info',
            'message':'Tasks added',
            'task_id':new_task.id
        })



# API: Toggle
@task_bp.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_status(task_id):
    if 'user_id' not in session:
        return jsonify({"state":"danger","message":"Unauthorized"}), 401

    task = Task.query.filter_by(id=task_id, user_id=session['user_id']).first()

    if task:
        if task.status == 'pending':
            new_status = 'working'
        elif task.status == 'working':
            new_status = 'completed'
        else:
            new_status = 'pending'
        task.status = new_status
        db.session.commit()
        return jsonify({
            'state':'success',
            'new_status':new_status
        })




# API: Delete
@task_bp.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'user_id' not in session:
        return jsonify({"state":"danger","message":"Unauthorized"}), 401

    task = Task.query.filter_by(id=task_id, user_id=session['user_id']).first()

    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({
            'state':'success',
            'message':'Task deleted successfully',
        })

#API : Clear all tasks
@task_bp.route('/clear', methods=['POST'])
def clear_tasks():
    if 'user_id' not in session:
        return jsonify({"state":"danger","message":"Unauthorized"}), 401

    Task.query.filter_by(user_id=session['user_id']).delete()
    db.session.commit()

    return jsonify({
        'state':'success',
        'message':'All tasks cleared successfully',
    })

@task_bp.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    task = Task.query.filter_by(id=task_id, user_id=session['user_id']).first()

    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if task:
        task.title = title
        task.description = description
        db.session.commit()

        return jsonify({
            "state":"success",
            "message":"Task updated"
        })