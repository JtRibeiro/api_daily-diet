from database import db

class Diet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), default=db.func.now())
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat() if self.created_at else None, 
            "is_active": self.is_active
        }




