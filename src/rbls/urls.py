from django.conf.urls import url
from . import views

app_name = 'rbls'

urlpatterns = [
    url(r'^list$', views.RBLView.as_view(), name='list'),
    url(r'^check$', views.RBLCheck.as_view(), name='check'),
]
