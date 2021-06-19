from django.conf.urls import url
from tutorials import views

urlpatterns = [
    url(r'^api/pizzas$', views.tutorial_list),
    url(r'^api/pizzas/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^home', views.home),
]
