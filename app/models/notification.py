from app.extensions import db

class Notification(db.Model):
    __tablename__ = 'notification'
    
    notification_id = db.Column(db.String, primary_key=True)
    raised_by = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Relationships
    raised_user = db.relationship("User", backref="notifications_raised")
