from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Coupon_List
import datetime
# Create your views here.

def display(request):

    res = get_entries(request)
    
    return HttpResponse(res)
    return render(request, "hello.html", {})

def new_entry(request):
    if ("company" in request.GET):
        add_entry(request)
    return render(request, "new_entry.html", {})
def add_entry(request):

    cl = Coupon_List(
        company=request.GET["company"],
        code = request.GET["code"],
        expiry = request.GET["expiry"],
        description = request.GET["description"],
        used= False
    )

    cl.save()

    # return render(request, "new_entry.html", {})

def remove_entry(request):
    pass
def modify_entry(request):
    pass
def get_entries(request):

    comp=""
    if ("company" in request.GET):
        comp  = request.GET["company"]
    
    if (comp!=""):
        objects = Coupon_List.objects.filter(company = comp,used = False)
    else:
        objects = Coupon_List.objects.all()
    
    res ='Printing all Coupon entries in the DB : <br>'
    # objects = objects.filter(request.GET["company"])
    for elt in objects:
        res += elt.company + " \t" + elt.code + " \t" + str(elt.expiry) + " " +  elt.description+"<br>"
    

    return res


