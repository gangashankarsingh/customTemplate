from django.urls import path 

from . import views 

urlpatterns = [


    #path("getTemplate", views.TemplateAndPlaceholdersView.as_view()),
    path("getTemplate", views.TemplateAndPlaceholdersViewUpdated.as_view()),

    
]