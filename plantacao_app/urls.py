from django.urls import include, path

from . import views

app_name = 'plantacao_app'
urlpatterns = [
    path('', views.home, name='index'),
    path('info', views.recebe_informacoes, name="info"),
    path('results',views.result_response, name="results"),
    path('saveInfo', views.saveInfo, name='saveInfo'),
    path('deleteAllInfo', views.deleteAllInfo, name='deleteAllInfo'),
    path('relatorios', views.relatorios, name='relatorios')
]
