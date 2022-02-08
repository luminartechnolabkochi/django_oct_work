from django.urls import path
from wcapp import views
urlpatterns=[
    path("",views.WordCountView.as_view(),name="wordcount")
]