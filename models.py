from app import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


events_categories_association = db.Table(
    "events_categories",
    db.metadata,
    db.Column("event_id", db.Integer, db.ForeignKey("events.id")),
    db.Column("category_id", db.Integer, db.ForeignKey("categories.id"))
)


class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    host_name = db.Column(db.String)
    url = db.Column(db.String)
    planned_start = db.Column(db.DateTime)
    planned_end = db.Column(db.DateTime)
    estimated_duration = db.Column(db.Integer)
    description = db.Column(db.String)

    categories = db.relationship(
                                "Category",
                                secondary=events_categories_association
                                )

    def __init__(
                    self, 
                    title, 
                    host_name, 
                    url, 
                    categories, 
                    planned_start, 
                    estimated_duration,
                    description
        ):
        self.title = title
        self.host_name = host_name
        self.url = url
        self.categories = categories
        self.planned_start = planned_start
        self.estimated_duration = estimated_duration
        self.description = description

    def __repr__(self):
        return "{}".format(self.title)


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "{}".format(self.title)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    _password = db.Column(db.String(128), nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, password):
        self._password = bcrypt.generate_password_hash(password)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self._password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return "{}".format(self.username)
