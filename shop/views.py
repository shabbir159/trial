from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
	products=Product.objects.all()
	n = len(products)
	total_card=n+3
	lst=[]
	for i in range(4,n+4):
	    lst.append(i)
	nSlides= n//1 + ceil((n/1) + (n//1))
	allProds = []
	catprods = Product.objects.values('category', 'id')
	cats = {item['category'] for item in catprods}
	for cat in cats:
	    prod = Product.objects.filter(category=cat)
	    n = len(prod)
	    nSlides = n // 4 + ceil((n / 4) - (n // 4))
	    allProds.append([prod, range(1, nSlides), nSlides])
 
	params={'Product':products,'allprods':allProds,'total':total_card,'no_of_slides': nSlides, 'range':range(1,10),'st':lst}
	return  render(request,'shop/index.html', params)

def about(request):
    return  render(request,'shop/about.html')
def contact(request):
    return HttpResponse('we are at about')
def tracker(request):
    return HttpResponse('we are at about')
def search(request):
    return HttpResponse('we are at about')
def productview(request):
    return HttpResponse('we are at about')
def checkout(request):
    return HttpResponse('we are at about')
