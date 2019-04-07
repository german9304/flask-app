from flask import (
    Blueprint, request, render_template, session
)
from ..models import (
    db, user, product
)
from sqlalchemy import desc
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


@storesBp.route('/top-products/', methods=['GET'])
def top_products():
    """Top 5 products by like."""
    products = product.Product.query. \
        order_by(desc(product.Product.likes)).all()[:6]
    context = {
        'products': products
    }
    return render_template('stores/topstores.html', **context)

@storesBp.route('/product/<int:product_id>/', methods=['GET'])
def get_product(product_id):
    print(f'product id is {product_id}')
    try:
        selected_product = product.Product.query.filter(product.Product.id == product_id) \
            .first()
        context = {
            'product': selected_product
        }
        print(selected_product.name)
    except Exception as e:
        print('An error ocurred')
        print(e)
    return render_template('stores/product.html', **context)