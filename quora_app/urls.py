from django.urls import path
from .views import *
from .question_views import *

urlpatterns = [
    path('signup/',signup,name='signup'), ###### Signup url
    path('',signin,name='signin'),  ####### Signin url
    path('logout/',logout_user,name='logout'),  ### logout url
    path('home/',home,name='home'),
    path('all_posts/',all_posts,name='all_posts'),
    path('post_detail/<int:post_id>/', post_detail, name='post_detail'),
    path('add_comment/<int:post_id>/', add_comment, name='add_comment'),
    path('like_post/<int:post_id>/', like_post, name='like_post'),
    # path('individual_posts/', individual_posts, name='individual_posts'),
]