from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Coupon_List
import datetime
# Create your views here.

def home(request):
    return render(request,"home.html",{})

def display(request):

    res=get_entries(request)
    # if ("company" in request.GET and "code" in request.GET and "modify" in request.GET and request.GET["modify"]):
    #     modify_entry(request)
    if ("info" in request.GET  and "modify" in request.GET and request.GET["modify"]):
        modify_entry(request)
    # return HttpResponse(res)
    return render(request, "display.html", {"res":res})

def new_entry(request):
    if ("company" in request.GET):
        add_entry(request)
        # remove_entry(request)
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
    
    #removes al entries where used flag is true
    objects = Coupon_List.objects.filter(used = True)
    
    objects.delete()


def modify_entry(request):
    s=request.GET["info"]
    print(s)
    s=s[1:len(s)-1]
    l=s.split(",")
    # print(l)
    comp=request.GET["info"]
    cod = request.GET["info"]
    # print(comp,cod)
    obj = Coupon_List.objects.filter(company = comp,code = cod).update(used=True)
    

    # remove_entry("")


def get_entries(request):

    comp=""
    if ("company" in request.GET):
        comp  = request.GET["company"]
    
    if (comp!=""):
        objects = Coupon_List.objects.filter(company = comp,used = False)
    else:
        objects = Coupon_List.objects.all()
    
    res =[]
    # objects = objects.filter(request.GET["company"])
    for elt in objects:
        # res.append( elt.company + " \t" + elt.code + " \t" + str(elt.expiry) + " " +  elt.description+ str(elt.used) )
        res.append( [elt.company , elt.code , str(elt.expiry), elt.description, str(elt.used)] )
    
    # f=open("display.html","w")
    # print(res)
    # f.write((res))
    # print(f.read())
    
    return res


