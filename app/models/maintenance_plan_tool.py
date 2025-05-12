from app.extensions import db

class MaintenancePlanTool(db.Model):
    __tablename__ = 'maintenance_plan_tool'
    id = db.Column(db.Integer, primary_key=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('maintenance_plan.plan_id'))
    tool_id = db.Column(db.Integer, db.ForeignKey('tool.tool_id'))
