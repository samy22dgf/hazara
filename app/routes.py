from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('routes',__name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')