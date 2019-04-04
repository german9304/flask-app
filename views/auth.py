from flask import (
    Blueprint, request, render_template
)
from ..models import (
    db, user, product
)


"""Init flask blue print"""
authBp = Blueprint('auth', __name__)


@authBp.route('/register/')
def register():
    print('register')
    return render_template('auth/register.html')

@authBp.route('/login/')
def login():
    print('register')
    return render_template('auth/login.html')