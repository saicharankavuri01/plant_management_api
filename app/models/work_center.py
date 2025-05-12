from app.extensions import db

class WorkCenter(db.Model):
    __tablename__ = 'work_center'
    work_center_id = db.Column(db.String, primary_key=True)
    description = db.Column(db.Text)
    cost_center = db.Column(db.String)
    rate_per_hour = db.Column(db.Numeric)
    capacity_hours_per_day = db.Column(db.Integer)
    responsible_person = db.Column(db.String)

    task_lists = db.relationship("TaskList", backref="work_center", lazy=True)
    maintenance_plans = db.relationship("MaintenancePlan", backref="work_center", lazy=True)
