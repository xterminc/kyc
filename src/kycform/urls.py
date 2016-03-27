from django.conf.urls import url
from . import views

app_name = 'kycform'

urlpatterns = [
    url(r'^$', views.form, name='form')
]
