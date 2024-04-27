from flask import render_template, Blueprint


admin_bp = Blueprint('admin_bp', __name__)


@admin_bp.route('/')
@admin_bp.route('/index')
def index_admin():
    return render_template('admin/index.html', title='Главная')