from core.utils import Mixin
from .base import db


class Invention(Mixin, db.Model):
    """Inventions Table."""

    __tablename__ = "invention"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    date = db.Column(db.Integer, nullable=False)
    origin = db.Column(db.String, nullable=True)
    inventor = db.Column(db.String, nullable=True)
    site = db.Column(db.String, nullable=True)

    def __init__(self, name, date, origin=None, inventor=None, site=None):
        self.name = name
        self.date = date
        self.origin = origin
        self.inventor = inventor
        self.site = site

    def __repr__(self):
        return f"<Name {self.name} - {self.date}>"
