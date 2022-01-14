from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Coupon_List
import datetime
# Create your views here.

def display(request):

    print("Request is ")
    print(request)
    print(type(request))
    text = """<h1>welcome to my app !</h1>"""
    add_entry("")
    res = get_entries("")
    
    return HttpResponse(res)
    return render(request, "/hello.html", {})

def add_entry(request):
    cl = Coupon_List(
        company="Swiggy",
        code = "ABC123",
        expiry = datetime.datetime(2015, 10, 9, 23, 55, 59),
        description = "60% off upto Rs 200. No minimum spend",
        used= False
    )

    cl.save()

def remove_entry(request):
    pass
def modify_entry(request):
    pass
def get_entries(request):

    objects = Coupon_List.objects.all()
    res ='Printing all Dreamreal entries in the DB : <br>'
   
    for elt in objects:
        res += elt.company + " \t" + elt.code + " \t" + elt.description+"<br>"

    return res


