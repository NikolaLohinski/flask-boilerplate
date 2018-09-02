from server.core import Mixin
from .base import db


class Invention(Mixin, db.Model):
    """Inventions Table."""

    __tablename__ = "invention"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    info = db.Column(db.String, nullable=True)
    year = db.Column(db.Integer, nullable=False)

    def __init__(self, name, year, info=None):
        self.name = name
        self.info = info
        self.year = year

    def __repr__(self):
        return f"<Name {self.name}>"
