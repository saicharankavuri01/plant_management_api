from app.extensions import db

class Tool(db.Model):
    __tablename__ = 'tool'
    tool_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    quantity = db.Column(db.Integer)
    serial_no = db.Column(db.String)
    last_calibrated = db.Column(db.Date)
