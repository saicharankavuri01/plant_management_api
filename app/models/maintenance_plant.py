from app.extensions import db

class MaintenancePlant(db.Model):
    __tablename__ = 'maintenance_plant'
    plant_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.Text)
    state = db.Column(db.String(50))
    country = db.Column(db.String(50))

    functional_locations = db.relationship("FunctionalLocation", backref="plant", lazy=True)
