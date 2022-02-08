from django.urls import path
from owner import views
# owner/books/100
urlpatterns=[
    path("home",views.owner_home),
    path("books/add",views.add_book),
    path("books/all",views.lis_book),
   path("books/<int:id>",views.book_detail)

]