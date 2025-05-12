from app.extensions import db

class MaintenancePlan(db.Model):
    __tablename__ = 'maintenance_plan'
    plan_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    equipment_id = db.Column(db.String, db.ForeignKey('equipment.equipment_id'), nullable=True)
    fl_id = db.Column(db.String, db.ForeignKey('functional_location.fl_id'), nullable=True)
    frequency_type = db.Column(db.String)
    frequency_value = db.Column(db.Integer)
    frequency_unit = db.Column(db.String)
    offset = db.Column(db.Integer)
    strategy = db.Column(db.String)
    work_center_id = db.Column(db.String, db.ForeignKey('work_center.work_center_id'))
    task_list_id = db.Column(db.String, db.ForeignKey('task_list.task_list_id'))
    is_active = db.Column(db.Boolean, default=True)
    last_executed_at = db.Column(db.Date)
    next_due_date = db.Column(db.Date)
