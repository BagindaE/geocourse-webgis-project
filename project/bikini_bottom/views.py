from django.shortcuts import render

# Create your views here.
def home(reuqest):
    return render(request,'pages/home.html')