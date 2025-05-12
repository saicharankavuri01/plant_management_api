from app.extensions import db

class MaintenancePlanMaterial(db.Model):
    __tablename__ = 'maintenance_plan_material'
    id = db.Column(db.Integer, primary_key=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('maintenance_plan.plan_id'))
    material_id = db.Column(db.Integer, db.ForeignKey('material.material_id'))
