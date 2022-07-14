from pydoc import describe
from django.shortcuts import render
from home.models import CustInsert
from datetime import date as date_n 


# Create your views here.

def home(request):
    return render(request,'home.html')

def recognize(request):
    return render(request,'home_page2.html')

def Insertrecord(request):
    context={'success':False}
    if request.method=="POST":
            saverecord=CustInsert()
            saverecord.name=request.POST.get('name')
            saverecord.address=request.POST.get('address')
            saverecord.amount=request.POST.get('amount')
            saverecord.item_type=request.POST.get('item_type')
            saverecord.description=request.POST.get('description')
            saverecord.save()
            data = CustInsert.objects.last()
            return render(request,'home_page3.html',{'c' : data})
    else:
        return render(request,'home_page2.html')

def Viewloan(request):  
    return render(request, 'view_loan.html')

def search(request):  
    if request.method == "POST":
        query_name = request.POST.get('name',None)
        if query_name:
            results = CustInsert.objects.filter(id__contains=query_name)
            return render(request, 'view_loan.html', {"results":results})
    return render(request, 'view_loan.html')

def calculate(request):
    return render(request, 'calculate.html')

def interest_calculation(request):
    if request.method == "POST":
        query_name = request.POST.get('id',None)
        date2= request.POST.get('currdate',None)
        if(query_name):
            results = CustInsert.objects.filter(id__contains=query_name)
            for d in results:
                date1=d.loan_date.date().strftime('%Y-%m-%d')
                principle=d.amount
            rate=5
            date1=date1.split('-')
            date2=date2.split('-')
            date_1 = date_n(int(date1[0]),int(date1[1]),int(date1[2]))  
            date_2 = date_n(int(date2[0]),int(date2[1]),int(date2[2]))
            no_of_days=(date_2 - date_1).days 
            i=(principle*rate*no_of_days/365)/100
            a=principle+i
            return render(request, 'calculate.html',{"p":principle,"interest":i,"amount":a,"success":True})
    return render(request, 'calculate.html')
