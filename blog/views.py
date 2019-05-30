from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.core.paginator import Paginator
from django.utils import timezone

# Create your views here.

def home(request):
    blogs = Blog.objects    #admin에 써져있는 목록들
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page') # get방식으로 페이지 번호를 알아왔다.
    posts = paginator.get_page(page) # 그 페이지 번호가 뭔지 넣어버림
    return render(request, 'home.html', {'blogs' : blogs, 'posts':posts}) # key랑 value값 리턴

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'detail' : details})
    # 우리가 앞에서 처음에 했을 때 blogobject로 받아온것들을 얻어올려고 하는것
    # 갖고오면 내용 보여주고 실패하면 404에러 띄워줌

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))    # 요청한걸 받아서 출력해주는 것

def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/' + str(blog.id))
    return render(request,'edit.html',{'blog':blog})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()       # 삭제 함수
    return redirect('/')    # 새로고침 그런느낌