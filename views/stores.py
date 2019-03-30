from flask import (
    Blueprint, request, render_template
)

"""Init flask blue print"""
storesBp = Blueprint('stores', __name__)

@storesBp.route('/')
@storesBp.route('/stores/')
def stores():
    """Route for stores."""
    return render_template('stores/stores.html')

@storesBp.route('/create-store/')
def create_store():
    """Create store route."""
    return render_template('stores/createstore.html')

@storesBp.route('/add-store/')
def add_store():
    return render_template('stores/store.html')

@storesBp.route('/top-stores/')
def top_stores():
    return render_template('stores/topstores.html')
