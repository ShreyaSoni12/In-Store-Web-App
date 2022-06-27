from pydoc import describe
from django.shortcuts import render
from home.models import CustInsert


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
            context={'success':True}
            data = CustInsert.objects.last()
            
            return render(request,'home_page3.html',{'c' : data})
    else:
        return render(request,'home_page2.html')

# def Viewrecord(request):
  
    
#     data = CustInsert.objects.last()
#     print(data.id)
#     return render(request, 'loan.html',{'c' : data})
