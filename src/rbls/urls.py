from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list$', views.RBLView.as_view(), name='list'),
    url(r'^check$', views.RBLView.as_view(), name='check'),
]