from app.extensions import db

class FunctionalLocation(db.Model):
    __tablename__ = 'functional_location'
    fl_id = db.Column(db.String, primary_key=True)
    fl_name = db.Column(db.String(100))
    plant_id = db.Column(db.String, db.ForeignKey('maintenance_plant.plant_id'), nullable=False)
    parent_fl_id = db.Column(db.String, db.ForeignKey('functional_location.fl_id'), nullable=True)
    structure_indicator = db.Column(db.String(1))  # e.g., A, B, C
    category = db.Column(db.String(20))            # e.g., PLANT, AREA, SYSTEM
    cost_center = db.Column(db.String(50))
    description = db.Column(db.Text)

    equipment = db.relationship("Equipment", backref="functional_location", lazy=True)
