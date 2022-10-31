from flask import Blueprint, current_app, abort
from flask_admin import Admin
from flask_admin.menu import MenuLink
from os.path import dirname, join
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView


admin_bp = Blueprint('Admin', __name__)


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def Home(self):
        return self.render('admin/index.html')
 
admin = Admin(current_app, name='Admin',
              template_mode='bootstrap3', index_view=MyAdminIndexView())

current_app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True



class ImportarArquivosAtualizacaoImpostos(ModelView):
    pass


class NotasFiscais(ModelView):
    pass

class NotasFiscais(ModelView):
    pass

class IPI(ModelView):
    pass

class ICMS(ModelView):
    pass

class CFOP(ModelView):
    pass

class NCM(ModelView):
    pass


'''
admin.add_view(IPI(name='IPI', endpoint='IPI'))
admin.add_view(ICMS(name='ICMS', endpoint='ICMS'))
admin.add_view(CFOP(name='CFOP', endpoint='CFOP'))
admin.add_view(NCM(name='NCM', endpoint='NCM'))


admin.add_link(MenuLink(name='IPI', url='/IPI', category="Impostos"))
admin.add_link(MenuLink(name='ICMS', url='/ICMS', category="Impostos"))
admin.add_link(MenuLink(name='CFOP', url='/CFOP', category="Impostos"))
admin.add_link(MenuLink(name='NCM', url='/NCM', category="Impostos"))

admin.add_sub_category(name="Impostos", parent_name="Impostos")
'''