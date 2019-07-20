from django.shortcuts import render
from . request import make_call

# Create your views here.

def index(request):
    data=make_call()
    records=data["records"]

    title='Xmusic'
    return render(request,'index.html',{'title':title,"records":records})
