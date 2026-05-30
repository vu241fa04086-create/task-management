from models.task_model import Task
from config.database import db


def add_task_service(data, user_id):

    task = Task(
        title=data.get("title"),
        description=data.get("description"),
        user_id=user_id
    )

    db.session.add(task)
    db.session.commit()

    return {
        "message": "Task added successfully"
    }, 201


def get_tasks_service(user_id):

    tasks = Task.query.filter_by(user_id=user_id).all()

    output = []

    for task in tasks:
        output.append({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status
        })

    return output


def update_task_service(task_id, data, user_id):

    task = Task.query.filter_by(id=task_id, user_id=user_id).first()

    if not task:
        return {"message": "Task not found"}, 404

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)

    db.session.commit()

    return {
        "message": "Task updated successfully"
    }, 200


def patch_status_service(task_id, data, user_id):

    task = Task.query.filter_by(id=task_id, user_id=user_id).first()

    if not task:
        return {"message": "Task not found"}, 404

    allowed_status = [
        "not started",
        "ongoing",
        "completed"
    ]

    status = data.get("status")

    if status not in allowed_status:
        return {"message": "Invalid status"}, 400

    task.status = status

    db.session.commit()

    return {
        "message": "Task status updated"
    }, 200


def delete_task_service(task_id, user_id):

    task = Task.query.filter_by(id=task_id, user_id=user_id).first()

    if not task:
        return {"message": "Task not found"}, 404

    db.session.delete(task)
    db.session.commit()

    return {
        "message": "Task deleted successfully"
    }, 200