from flask import (
    Blueprint, request, render_template, session
)
from ..models import (
    db, user, product
)
from .data import PRODUCTS

"""Init flask blue print"""
storesBp = Blueprint('stores', __name__)


@storesBp.route('/')
@storesBp.route('/stores/')
def stores():
    """Route for stores."""
    context = {
        'products': product.Product.query.all()
    }
    # for item in product.Product.query.all():
    #     print(item.name)
    return render_template('stores/stores.html', **context)


@storesBp.route('/create-product/', methods=['POST', 'GET'])
def create_product():
    """Create product route."""
    print(request.method)
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        description = request.form['description']
        print(f'name:{name} qty:{quantity} descr:{description}')

    return render_template('stores/createproduct.html')


@storesBp.route('/add-store/')
def add_store():
    return render_template('stores/store.html')


@storesBp.route('/top-stores/')
def top_stores():
    return render_template('stores/topstores.html')
