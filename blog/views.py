from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib import messages
from .models import BlogPost, Feature


# Create your views here.
def blog(request):
    blogPost = BlogPost.objects.all()
    print(blogPost)

    feature = Feature.objects.all()

    context = {'blogPost': blogPost, 'feature': feature}
    return render(request, 'blog/blog.html', context)


def blogPost(request, slug):
    post = BlogPost.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()

    param = {'post': post}

    return render(request, 'blog/blogPost.html', param)



