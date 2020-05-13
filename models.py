from app import db


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
    planned_date = db.Column(db.DateTime)

    categories = db.relationship("Category",
                                 secondary=events_categories_association)

    def __init__(self, title, host_name, url, categories):
        self.title = title
        self.host_name = host_name
        self.url = url
        self.categories = categories

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
