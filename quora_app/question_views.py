from django.shortcuts import render, redirect
from .forms import *

def home(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(
                user=request.user,
                heading=form.cleaned_data['heading'],
                description=form.cleaned_data['description'],
                likes=0  # Set the initial likes to 0
            )
            post.save()
            return redirect('home')  # Redirect to the homepage after creating a post

    else:
        form = PostForm()

    # Retrieve and filter user-specific posts
    user_posts = Post.objects.filter(user=request.user)

    return render(request, 'home.html', {'form': form, 'user_posts': user_posts})




# def individual_posts(request):
#     user = request.user
#     user_posts = Post.objects.filter(user=user)

#     return render(request, 'home.html', {'user_posts': user_posts})


def all_posts(request):
    # user = request.user
    all_posts = Post.objects.all()
    return render(request,'all_posts.html',{'all_posts':all_posts})