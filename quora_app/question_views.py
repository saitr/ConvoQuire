from django.shortcuts import render, redirect
from .forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required 
@login_required(login_url='/signin/')

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






@login_required(login_url='/signin/')
def all_posts(request):
    all_posts = Post.objects.all()
    return render(request,'all_posts.html',{'all_posts':all_posts})

@login_required(login_url='/signin/')

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'all_posts.html', {'post': post, 'comments': comments})

@login_required(login_url='/signin/')   
def add_comment(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            comment = Comment(
                post=post,
                user=request.user,
                comment=comment_text
            )
            comment.save()

    return HttpResponseRedirect(reverse('all_posts'))



@csrf_exempt
@login_required(login_url='/signin/')
@require_POST
def like_post(request,post_id):
    post_id = request.POST.get('post_id')
    post = Post.objects.get(pk=post_id)
    post.likes += 1
    post.save()
    response_data = {
        'like_count': post.likes,
    }
    return JsonResponse(response_data)
