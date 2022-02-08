from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from owner.models import books


# class based views, function based

def owner_home(request):
    return render(request,"index.html")

def add_book(request):
    if request.method=="GET":
        print("inside get")
        return render(request,"addbook.html")
    else:
        print("am inside post ")
        print(request.method)
        return render(request, "addbook.html")


def lis_book(request):
    context={"books":books}
    return render(request,"booklist.html",context)

# owner/books/100

def book_detail(request,id):
    book=[book for book in books if book["id"]==id]
    context={"book":book}
    return render(request,"bookdetail.html",context)

