from django.urls import path
from app_empresa import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('empresas/', views.listagem_empresas, name='listagem_empresas'),
    path('empresas/editar/<int:id>/', views.editar_empresa, name='editar_empresa'),
    path('empresas/excluir/<int:id>/', views.excluir_empresa, name='excluir_empresa'),
    path('api/valida-cnpj/', views.valida_cnpj, name='valida_cnpj'),
    path('api/consulta-cep/', views.consulta_cep, name='consulta_cep'),
    path('api/lista-cidades/<str:uf>/', views.lista_cidades, name='lista_cidades'),
]