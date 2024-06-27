# app/routes.py

from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/register')
def register():
    return render_template('register.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Add routes for managing expenses, budgets, and goals here

# Example:
@bp.route('/expenses')
@login_required
def expenses():
    return render_template('expenses.html')

@bp.route('/budgets')
@login_required
def budgets():
    return render_template('budgets.html')

@bp.route('/goals')
@login_required
def goals():
    return render_template('goals.html')
