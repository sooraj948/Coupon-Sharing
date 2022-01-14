from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Coupon_List
import datetime
# Create your views here.

def display(request):

    print("Request is ")
    print(request)
    print(type(request))
    # print(request.GET["company"])
    text = """<h1>welcome to my app !</h1>"""
    # add_entry("")
    res = get_entries(request)
    
    return HttpResponse(res)
    # return render(request, "/hello.html", {})

def add_entry(request):
    cl = Coupon_List(
        company="Zomato",
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

    comp=""
    if ("company" in request.GET):
        comp  = request.GET["company"]
    
    if (comp!=""):
        objects = Coupon_List.objects.filter(company = comp)
    else:
        objects = Coupon_List.objects.all()
    
    res ='Printing all Coupon entries in the DB : <br>'
    # objects = objects.filter(request.GET["company"])
    for elt in objects:
        res += elt.company + " \t" + elt.code + " \t" + elt.description+"<br>"
    

    return res


