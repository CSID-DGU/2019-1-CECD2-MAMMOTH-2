from django.shortcuts import render
# Create your views here.

def main(request):
    return render(request, 'sfota/main.html',{})
def listdev(request):
    return render(request, 'sfota/listdev.html',{})
def listfirm(request):
    return render(request, 'sfota/listfirm.html',{})
