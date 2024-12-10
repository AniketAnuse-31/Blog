from django.shortcuts import render, redirect,get_object_or_404
from django.http import  Http404
from .models import BlogPost, Comment, User

# Create your views here.
def BlogView(request):
    blog = BlogPost.objects.all()
    return render(request, 'blog_view.html',{'blogs':blog})

def BlogCreate(request):
    if request.method == 'POST':
        title = request.POST.get('title','')
        content = request.POST.get('content','')
        category = request.POST.get('category','')
        user = request.user
        BlogPost.objects.create(title=title, content = content,author = user, category= category)
        return redirect('blog-view')
    return render(request, 'blog_create.html')

def BlogUpdate(request, id):
    blog = BlogPost.objects.get(id = id)
    if request.method == 'POST':
        blog.title = request.POST.get('title','')
        blog.content = request.POST.get('content','')
        blog.category = request.POST.get('category','')
        blog.save()
        return redirect('blog-view')
    return render(request, 'blog_update.html', {'blog':blog})

def BlogDelete(request, id):
    blog = BlogPost.objects.get(id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog-view')
    return render(request, 'blog_delete.html')

def CommentAdd(request, id):
    if request.method == 'POST':
        post = get_object_or_404(BlogPost, id=id)
        content = request.POST.get('content', '')
        Comment.objects.create(post=post,user=request.user, content = content)
        return redirect('blog-view')
    return render(request, 'comment_add.html', )
               
def CommentView(request, id):
    comment = Comment.objects.get(id=id)
    if comment.exists() != True:
        return redirect('comment-add')
    return render(request, 'comment_view.html', {'comment':comment})
    
def CommentDelete(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        comment.delete()
        return redirect('blog-view')
    return render(request, 'comment_delete.html')