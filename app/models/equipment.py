from app.extensions import db

class Equipment(db.Model):
    __tablename__ = 'equipment'
    equipment_id = db.Column(db.String, primary_key=True)
    fl_id = db.Column(db.String, db.ForeignKey('functional_location.fl_id'), nullable=False)
    equipment_description = db.Column(db.String(100))
    serial_number = db.Column(db.String)
    manufacturer = db.Column(db.String)
    model = db.Column(db.String)
    install_date = db.Column(db.Date)
    last_service_at = db.Column(db.Date)
    criticality = db.Column(db.String)

    maintenance_plans = db.relationship("MaintenancePlan", backref="equipment", lazy=True)
