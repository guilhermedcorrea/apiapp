from flask import Blueprint, current_app, abort, render_template, redirect, url_for
from flask_admin import Admin
from flask_admin.menu import MenuLink
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, HiddenField, SelectField
from flask_wtf.file import FileField, FileAllowed
from sqlalchemy import select, join
from datetime import datetime, timedelta
from sqlalchemy import func
from datetime import date

admin_bp = Blueprint('Admin', __name__)
from ..extensions import db

from ..models.notas_hausz_mapa import NotaFiscal, NotaFiscalItens
from ..models.cliente_hausz_mapa import Cliente
from ..models.pedidos_hausz_mapa import PedidoFlexy

class AddProduct(FlaskForm):
    name = StringField('Name')
    price = IntegerField('Price')
    stock = IntegerField('Stock')
    description = TextAreaField('Description')
    #image = FileField('Image', validators=[FileAllowed(IMAGES, 'Only images are accepted.')])


@admin_bp.route('/admin/')
@admin_bp.route('/admin')
def admin():
     with db.engine.connect() as conn:
        query = (select(NotaFiscal,PedidoFlexy).join(NotaFiscal,
            PedidoFlexy.CodigoPedido == NotaFiscal.CodigoPedido).filter(
                NotaFiscal.DataEmissao >  date.today()-timedelta(weeks=20)))
        exec = conn.execute(query).all()
        query_dicts = [{key: value for (key, value) in row.items()} for row in exec]
        
        return render_template('admin/index.html', admin=True, notas=query_dicts)

@admin_bp.route('/admin/add', methods=['GET', 'POST'])
def add():
    form = AddProduct()

    if form.validate_on_submit():
       
        return redirect(url_for('admin'))

    return render_template('admin/add-product.html', admin=True, form=form)


@admin_bp.route('/admin/order/<order_id>')
def order(order_id):


    return render_template('admin/view-order.html', order=order, admin=True)

@admin_bp.route("/")
def index():
    return redirect(admin)