from app.extensions import db

class Material(db.Model):
    __tablename__ = 'material'
    material_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    lead_time = db.Column(db.Integer)
    cost = db.Column(db.Numeric)
    unit_of_measure = db.Column(db.String)
    material_type = db.Column(db.String)  # spares or non_value
