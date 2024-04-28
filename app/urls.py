from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('page_login', views.page_login, name='page_login'),
    path('logout/', views.app_logout, name='app_logout'),
    path('list/<int:list_id>/', views.todo_list, name='todo_list'),
    path('list/<int:list_id>/add/', views.add_item, name='add_item'),
    path('list/<int:list_id>/remove/<int:item_id>/', views.remove_item, name='remove_item'),
    path('list/<int:list_id>/done/<int:item_id>/', views.done_item, name='done_item'),
#especialidade
    path('listar_especialidades', views.listar_especialidades, name='listar_especialidades'),
    path('especialidades/new/', views.cadastrar_especialidade, name='cadastrar_especialidade'),

    path('listar_prestadores', views.listar_prestadores, name='listar_prestadores'),
    path('prestador/<int:id>/', views.detalhar_prestador, name='detalhar_prestador'),
    path('prestador/new/', views.cadastrar_prestador, name='cadastrar_prestador'),
    #cliente
    path('listar_clientes', views.listar_clientes, name='listar_clientes'),
    path('cliente/<int:id>/', views.detalhar_cliente, name='detalhar_cliente'),
    path('cliente/new/', views.cadastrar_cliente, name='cadastrar_cliente'),
    #agenda
    path('listar_agenda', views.listar_agenda, name='listar_agenda'),
    path('agenda/new/', views.cadastrar_agenda, name='cadastrar_agenda'),
    path('atendimento/new/', views.cadastrar_atendimento, name='cadastrar_atendimento'),
]