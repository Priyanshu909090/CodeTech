from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.contrib import messages
from blog.models import BlogPost, Feature
# Create your views here.
from .models import Contact
from django.contrib.auth.models import User


def home(request):
    feature = Feature.objects.all()
    posts = BlogPost.objects.all()

    vox = {'feature': feature, 'posts': posts}
    return render(request, 'home/home.html', vox)


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', "")
        email = request.POST.get('name', '')
        phone = request.POST.get('name', '')
        textarea = request.POST.get('name', '')
        if len(name) < 2 and len(email) < 8 and len(phone) < 10 and len(textarea) < 4:
            messages.error(request, 'Enter Details Correctly')
        else:
            contact = Contact(name=name, email=email, phone=phone, textarea=textarea)
            contact.save()
            messages.success(request, 'Successfully sent')
    return render(request, 'home/contact.html')


def search(request):
    query = request.GET.get('query')

    if len(query) > 73:
        blogPost = []
    else:
        blogPostTitle = BlogPost.objects.filter(title__icontains=query)
        blogPostContent = BlogPost.objects.filter(content__icontains=query)
        blogPostAuthor = BlogPost.objects.filter(author__icontains=query)
        blogPost = blogPostTitle.union(blogPostContent, blogPostAuthor)

    if blogPost.count == 0:
        messages.warning(request, 'Sorry! Can not found results')
    params = {'blogPost': blogPost, 'query': query}
    return render(request, 'home/search.html', params)


def signUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        pass2 = request.POST.get('pass2')

        if len(username) < 3 and len(fname) < 2 and len(lname) < 2 and len(email) < 8 and len(
                password) < 4 and password != pass2:
            messages.error(request, "Please Fill Your Form correctly")
        else:
            myUser = User.objects.create(username=username, email=email, password=password)
            myUser.first_name = fname
            myUser.last_name = lname
            myUser.save()

            messages.success(request, "Your CodeTech Account has been created Successfully")
            return redirect('home')

    else:
        messages.error(request, "Error- 404, can not reach page")


def signIn(request):
    if request.method == 'POST':
        loginUsername = request.POST.get('loginUsername')
        loginpass = request.POST.get('loginpass')
        user = authenticate(request, username=loginUsername, password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully Logged in')
            return redirect('home')
        else:
            messages.warning(request, 'Insufficient Details! Enter Your Details Correctly')
            return redirect('home')
    return redirect('home')


def logout1(request):
    logout(request)
    return redirect('home')


def feature(request):
    fpost = Feature.objects.all()

    param = {'fpost': fpost}

    return render(request, 'home/feature.html', param)
