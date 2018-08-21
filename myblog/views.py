from django.shortcuts import render

# Create your views here.


#主页
def index(request):
    return  render(request,'myblog/index.html')

#关于
def  about(request):
    return  render(request,'myblog/about.html')
def news(request):
    return render(request,'myblog/news.html')
def  product(request):
    return  render(request,'myblog/product.html')


def shownews(request):
    return  render(request,'myblog/shownews.html')

def  showproduct(request):
    return  render(request,'myblog/showproduct.html')


"""def  service(request):
    return  render(request,'myblog/service.html')

def  website_400tel(request):
    return  render(request,'myblog/website_400tel.html')

def   website_400tel_fee(request):
    return   render(request,'myblog/website_400tel_fee.html')
def   website_400tel_function(request):
    return   render(request,'myblog/website_400tel_function.html')

def  website_build(request):
    return   render(request,'myblog/website_build.html')

def  website_domain(request):
    return render(request,'myblog/website_domain.html')
def  website_hosting(request):
    return   render(request,'myblog/website_hosting.html')
def   website_revision(request):
    return   render(request,'myblog/website_revision.html')

def  website_webmastering(request):
    return   render(request,'myblog/website_webmastering.html')
"""

