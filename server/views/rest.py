import json
from flask import Blueprint, request
from ..models import db
from sqlalchemy.sql import func
from server.models import Invention
from server.core import create_response, serialize_list

rest = Blueprint('rest', __name__)


@rest.route('/inventions/all', methods=['GET'])
def get_all_inventions():
    inventions = Invention.query.all()
    return create_response(data={
        'inventions': serialize_list(inventions)
    })


@rest.route('/inventions/sample', methods=['POST'])
def get_sample_inventions():
    number = request.form['number']
    inventions = Invention.query.order_by(func.random()).limit(number)
    return create_response(data={
        'inventions': serialize_list(inventions)
    })


@rest.route('/add', methods=['POST'])
def add_invention():
    name = request.form['name']
    info = request.form['info']
    year = request.form['year']
    invention = Invention(name=name, info=info, year=year)
    db.session.add(invention)
    db.session.commit()
    return create_response(data=dict(request.form))


@rest.route('/add/batch', methods=['POST'])
def add_batch_inventions():
    inventions = request.get_json()
    for invention in inventions:
        db.session.add(Invention(
            name=invention['name'],
            info=invention['info'],
            year=invention['year']
        ))
    db.session.commit()
    return create_response(data={
        'inventions': json.dumps(inventions, indent=2)
    })


@rest.route('/del/id', methods=['POST'])
def delete_id():
    _id = request.form.get('id')
    invention = Invention.query.get(_id)
    db.session.delete(invention)
    db.session.commit()
    return create_response(data=dict(request.form))


@rest.route('/del/name', methods=['POST'])
def delete_name():
    name = request.form.get('name')
    invention = Invention.query.filter(Invention.name == name).first()
    db.session.delete(invention)
    db.session.commit()
    return create_response(data=dict(request.form))
