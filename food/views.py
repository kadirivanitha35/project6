from django.shortcuts import render

# Create your views here.
def burger(request):
    return render(request,'burger.html') 
