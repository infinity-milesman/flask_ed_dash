from app import db


class User_tbl(db.Model):
    __tablename__ = 'user_tbl'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(15))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256))

    def __repr__(self):
        return '<User %r>' % self.username