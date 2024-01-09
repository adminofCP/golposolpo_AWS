from django.shortcuts import render
from blog.models import Post,Catagory

# Create your views here.

#homepahge of blog app
def firstpage(request,url):
    post = Post.objects.get(urls=url)
    catagory = Catagory.objects.all()
    # print(post)
    posts = {'post':post,'catagory':catagory}
    return render(request,'BlogHome.html',posts)

def ViewCatagory(request,url):
    catagory = Catagory.objects.get(urls=url)
    post = Post.objects.filter(catagory=catagory)
    # print(post)
    posts = {'post':post,'catagory':catagory}
    return render(request,'ViewCatagory.html',posts)

def Search(request):
    name = request.GET.get("search")
    print(name)
    allPost = Post.objects.filter(title__icontains=name)
    param = {'post':allPost}
    return render(request,'Search_page.html',param)

def Contact(request):
    return render(request,'contactme.html')