from django.contrib.auth.decorators import login_required
from django.urls import include, path

from cadastros.views import CidadeList, CidadeDetail, CidadeDelete, CidadeCreate, CidadeUpdate, PaisList, PaisCreate, \
    PaisDetail, PaisDelete, PaisUpdate

urlpatterns = [
    path('', CidadeList.as_view(), name='cidades-list'),
    path('detail/<int:pk>/', CidadeDetail.as_view(), name='cidades-detalhe'),
    path('delete/<int:pk>/', login_required(CidadeDelete.as_view()), name='cidades-remove'),
    # path('update/', editar_cidade, name='cidades-editar'),
    path('update/<int:pk>/', login_required(CidadeUpdate.as_view()), name='cidades-editar'),
    path('create/', login_required(CidadeCreate.as_view()), name='cidades-cadastro'),
    path('paislist/', PaisList.as_view(), name='pais-list'),
    path('paiscreate/', login_required(PaisCreate.as_view()), name='pais-cadastro'),
    path('paisdetail/<int:pk>/', PaisDetail.as_view(), name='pais-detalhe'),
    path('paisdelete/<int:pk>/', login_required(PaisDelete.as_view()), name='pais-remove'),
    path('paisupdate/<int:pk>/', login_required(PaisUpdate.as_view()), name='pais-editar'),
]