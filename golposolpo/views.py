from django.shortcuts import render
from blog.models import Post,Catagory

#first page of web
def firstpage(request):
    #load all post from db(10)
    posts = Post.objects.all()[:11]
    catagory = Catagory.objects.all()
    # print(posts)
    posts = {'post':posts,'catagory':catagory}
    return render(request,'MainHome.html',posts)