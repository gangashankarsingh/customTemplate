from django.urls import path 

from . import views 

urlpatterns = [


    path("getTemplate", views.GetTemplate.as_view()),
]