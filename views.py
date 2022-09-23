from flask import (
    render_template, request, Blueprint, session, redirect, url_for
)

views = Blueprint(__name__, 'views')

@views.route('/')
def index():
    return render_template('index.html')