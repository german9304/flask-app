from flask import (
    Blueprint, request, render_template
)
from .data import PRODUCTS

"""Init flask blue print"""
storesBp = Blueprint('stores', __name__)

@storesBp.route('/')
@storesBp.route('/stores/')
def stores():
    """Route for stores."""
    context = {
        'products': PRODUCTS
    }
    return render_template('stores/stores.html', **context)

@storesBp.route('/create-product/')
def create_product():
    """Create product route."""
    return render_template('stores/createproduct.html')

@storesBp.route('/add-store/')
def add_store():
    return render_template('stores/store.html')

@storesBp.route('/top-stores/')
def top_stores():
    return render_template('stores/topstores.html')
