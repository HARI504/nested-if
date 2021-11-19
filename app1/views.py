from django.shortcuts import render

# Create your views here.
def nested(request):
    d={'a':100,'b':99,'c':101}
    return render(request,'h1.html',context=d)