from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^order/$', views.OrderView.as_view()),
]