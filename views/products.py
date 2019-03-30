from flask import Blueprint, request

"""Init flask blue print"""
pb = Blueprint('products', __name__)


@pb.route('/')
def create_product():
    req = request.json
    return {'product': req}



