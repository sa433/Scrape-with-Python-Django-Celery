from django.shortcuts import render
from selenium import webdriver
import time
from myapp.models import BookModel
from myapp.tasks import scrape

# Create your views here.
def home(request):
    books = BookModel.objects.all()
    if request.method == "POST":
        url = request.POST.get("url")
        r1 = scrape.delay(url)
        print("res1  = ",r1)
        if r1.successful():
            msg = "Extraction completed"
        else:
            msg = "Extraction under process"
        return render(request, "home.html", {'data':msg, 'books':books, 'r1':r1})
    else:
        return render(request,"home.html", {'books':books})

