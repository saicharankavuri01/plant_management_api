from app.extensions import db

class TaskListOperation(db.Model):
    __tablename__ = 'task_list_operation'
    id = db.Column(db.Integer, primary_key=True)
    task_list_id = db.Column(db.String, db.ForeignKey('task_list.task_list_id'), nullable=False)
    operation_number = db.Column(db.String)
    description = db.Column(db.Text)
    duration_hours = db.Column(db.Numeric)
    num_persons = db.Column(db.Integer)
    qualification_required = db.Column(db.String)
