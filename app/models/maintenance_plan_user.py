from app.extensions import db

class MaintenancePlanUser(db.Model):
    __tablename__ = 'maintenance_plan_user'
    id = db.Column(db.Integer, primary_key=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('maintenance_plan.plan_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
