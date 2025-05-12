from app.extensions import db

class WorkOrder(db.Model):
    __tablename__ = 'work_order'
    
    work_order_id = db.Column(db.String, primary_key=True)
    
    type = db.Column(db.String(20), nullable=False)  # 'planned' or 'unplanned'

    # Foreign Keys
    maintenance_plan_id = db.Column(db.Integer, db.ForeignKey('maintenance_plan.plan_id'), nullable=True)
    equipment_id = db.Column(db.String, db.ForeignKey('equipment.equipment_id'), nullable=True)
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=True)

    # Common attributes
    priority = db.Column(db.String(20))  # e.g., Low, Medium, High, Critical
    description = db.Column(db.Text)
    status = db.Column(db.String(20))  # planning, released, inprogress, confirmed
    estimated_cost = db.Column(db.Numeric)
    estimated_time_hours = db.Column(db.Numeric)
    material_availability = db.Column(db.String(20))  # available, partial, not-available

    # For unplanned work order
    steps_to_complete = db.Column(db.Text, nullable=True)

    # Relationships
    maintenance_plan = db.relationship("MaintenancePlan", backref="work_orders")
    equipment = db.relationship("Equipment", backref="work_orders")
    assigned_user = db.relationship("User", backref="assigned_work_orders")
