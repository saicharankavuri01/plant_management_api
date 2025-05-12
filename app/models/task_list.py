from app.extensions import db

class TaskList(db.Model):
    __tablename__ = 'task_list'
    task_list_id = db.Column(db.String, primary_key=True)
    description = db.Column(db.Text)
    equipment_category = db.Column(db.String)
    work_center_id = db.Column(db.String, db.ForeignKey('work_center.work_center_id'), nullable=False)
    operation_count = db.Column(db.Integer)
    status = db.Column(db.String)

    operations = db.relationship("TaskListOperation", backref="task_list", lazy=True)
    maintenance_plans = db.relationship("MaintenancePlan", backref="task_list", lazy=True)
