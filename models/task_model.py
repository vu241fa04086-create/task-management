from config.database import db


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(50), default="not started")

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    