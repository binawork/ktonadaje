from app import db
from sqlalchemy import Sequence


class Fleeb(db.Model):
    __tablename__ = 'fleebs'

    id = db.Column(db.Integer, Sequence('fleebs_id_seq'), primary_key=True)
    title = db.Column(db.String)
    host_name = db.Column(db.String)
    url = db.Column(db.String)
    category = db.Column(db.String(30))

    def __init__(self, title, host_name, url, category):
        self.title = title
        self.host_name = host_name
        self.url = url
        self.category = category

    def __repr__(self):
        return '<id {}'.format(self.id)
