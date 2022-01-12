from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def fotogallery(request):
    return render(request, 'mainapp/fotogalery.html')

def gologram(request):
    return render(request, 'mainapp/gologramma.html')

def beauty(request):
    return render(request, 'mainapp/index3.html')