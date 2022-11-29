from marshmallow import Schema, fields
from config import db


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(80), unique=True, nullable=False)
    color = db.Column(db.String(120), nullable=False)

    def __init__(self, pname, color):
        self.pname = pname
        self.color = color

    def __repr__(self):
        return self.pname

    @classmethod
    def getAll(cls):
        return cls.query.all()

    @classmethod
    def getById(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def exist(cls, pname):
        return bool(cls.query.filter_by(pname=pname).first())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class PeopleSchema(Schema):
    id = fields.Integer()
    pname = fields.String()
    color = fields.String()
