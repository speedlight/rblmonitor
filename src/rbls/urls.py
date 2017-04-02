from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.RBLView.as_view(), name='rbl_list'),
]