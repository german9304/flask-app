from flask import (
    Blueprint, request, render_template, url_for, session, redirect
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
        User = user.Users(email=email, username=username, password=password)
        # newUser = db.database.insert(User)
        # return redirect(url_for('home'))

    return render_template('auth/register.html')

@authBp.route('/login/', methods=['GET', 'POST'])
def login():
    """Log in User authentication."""
    if request.method == 'POST':
        # email = request.form['email']
        email = request.form['email']
        password = request.form['password']
        # print(type(email))
        # print(password)
        try:
            u = user.Users.query.filter(user.Users.email==email) \
            .one()
            if password == u.getPassword():
                print('equal passwords')
        except Exception as e:
            print(e)
        
    return render_template('auth/login.html')

@authBp.route('/logout/')
def logout():
    # email = request.form['email']
    # username = request.form['username']
    print('register')
    return redirect(url_for('home'))