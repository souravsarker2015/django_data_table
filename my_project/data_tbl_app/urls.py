from django.urls import path

from data_tbl_app.views import home

urlpatterns = [
    path('home/', home, name='home'),
]
