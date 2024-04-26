import sqlalchemy as sa
from flask import render_template, flash, url_for, redirect, request, Blueprint


admin_bp = Blueprint('admin_bp', __name__)


@admin_bp.route('/')
@admin_bp.route('/index')
def index_admin():
    return render_template('admin/index.html', title='Главная')