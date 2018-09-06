import os
import json
from flask import Blueprint, request
from ..models import db
from core.models import Invention
from core.utils import create_response, serialize_list

v0 = Blueprint('rest', __name__)


@v0.route('/inventions', methods=['GET'])
def get_all_inventions():
    inventions = Invention.query.order_by('date', 'name').all()
    return create_response(data={
        'inventions': serialize_list(inventions)
    })


@v0.route('/inventions/<int:_id>', methods=['GET'])
def get_invention(_id):
    return create_response(data={
        'inventions': Invention.query.get(_id).to_dict()
    })


@v0.route('/inventions/init', methods=['PUT'])
def re_init_db():
    db.drop_all()
    db.create_all()
    with open(os.environ['DEFAULT_INVENTIONS_FILE_PATH']) as stream:
        invention_list = json.load(stream)
    for invention in invention_list:
        db.session.add(
            Invention(
                name=invention.get('name'),
                date=invention.get('date'),
                origin=invention.get('origin'),
                inventor=invention.get('inventor'),
                site=invention.get('site')
            )
        )
    db.session.commit()
    return create_response(data={
        'inventions': invention_list
    }, message='Database re-initialized')


@v0.route('/inventions', methods=['POST'])
def post_inventions():
    invention = request.get_json()
    db.session.add(Invention(
        name=invention.get('name'),
        date=invention.get('date'),
        origin=invention.get('origin'),
        inventor=invention.get('inventor'),
        site=invention.get('site')
    ))
    db.session.commit()
    return create_response(data={
        'invention': invention
    }, message='Saved record')


@v0.route('/inventions/<int:_id>', methods=['DELETE'])
def delete_inventions(_id):
    invention = Invention.query.get(_id)
    if invention is None:
        raise Exception('Did not found record with id: %s' % _id)
    db.session.delete(invention)
    db.session.commit()
    return create_response(data={
        'invention': invention.to_dict()
    }, message='Record deleted')
