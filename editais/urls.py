from django.urls import path
from editais.views import edital_view, pergunta_view


app_name ='editais'

urlpatterns = [
    
    # ----------------------- Edital -------------------------------------------------#
    path('cadastrar/', edital_view.CriarEdital.as_view(), name='criar_edital'),
    path('editar/<int:pk>/', edital_view.EditarEdital.as_view(), name='editar_edital'),
    path('listar/editais/', edital_view.ListarEdital.as_view(), name='listar_editais'),
    path('detalhe/<int:id>/',edital_view.edital_view_adm,name='edital_detalhe'),
    path('remover/<int:pk>/', edital_view.RemoverEdital.as_view(), name='remover_edital'),

    # # ----------------------- Pergunta -------------------------------------------------#
    path('pergunta/criar_pergunta/<int:id>/',pergunta_view.pergunta_add, name='criar_pergunta'),
    # path('pergunta/editar_pergunta/<int:id>/',pergunta_view.editar_pergunta, name='editar_pergunta'),
    
    

]
