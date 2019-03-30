from flask import (
    Blueprint, render_template
)

bp = Blueprint('/home/', __name__)


def index():
    return render_template('base.html')
