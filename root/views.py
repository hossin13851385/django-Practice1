from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'index.html')

def pro(request):
    return render(request , 'portfolio.html')