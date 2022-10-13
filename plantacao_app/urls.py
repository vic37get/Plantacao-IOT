from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home),
    path('info', views.recebe_informacoes),
    path('results',views.result_response),
    path('saveInfo', views.saveInfo, name='saveInfo'),
    path('deleteAllInfo', views.deleteAllInfo, name='deleteAllInfo'),
    path('dashboard', views.dashboard, name='dashboard')
]
