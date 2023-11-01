from django.shortcuts import render, redirect
from .forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

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







def all_posts(request):
   
    all_posts = Post.objects.all()
    return render(request,'all_posts.html',{'all_posts':all_posts})

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'all_posts.html', {'post': post, 'comments': comments})


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
@require_POST
def like_post(request,post_id):
    post_id = request.POST.get('post_id')

    # Retrieve the post based on the post_id
    post = Post.objects.get(pk=post_id)

    # Increment the like count for the post
    post.likes += 1

    # Save the changes to the post
    post.save()

    # Return a JSON response with the new like count
    response_data = {
        'like_count': post.likes,
    }
    return JsonResponse(response_data)
