from flask import (
    Blueprint, render_template
)

homeBP = Blueprint('home', __name__)


@homeBP.route('/')
def index():
    return render_template('stores/stores.html')
