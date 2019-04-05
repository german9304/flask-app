from flask import (
    Blueprint, request, render_template, url_for, session
)
from ..models import (
    db, user, product
)


"""Init flask blue print"""
authBp = Blueprint('auth', __name__)


@authBp.route('/register/', methods=['GET', 'POST'])
def register():
    """This function registers user."""
    if request.method == 'POST':
        print(request.form)
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        print(f'username:{username} email:{email} password:{password}')

    return render_template('auth/register.html')

@authBp.route('/login/')
def login():
    print('register')
    return render_template('auth/login.html')