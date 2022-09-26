from flask import (Blueprint, render_template, request, flash, jsonify)
from flask_login import login_required, current_user
from .models import Product
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods =['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        product = request.form.get('product')
    return render_template('home.html', user = current_user)


