from django.urls import path
from .views import *
from .question_views import *

urlpatterns = [
    path('signup/',signup,name='signup'), ###### Signup url
    path('signin/',signin,name='signin'),  ####### Signin url
    path('logout/',logout_user,name='logout'),  ### logout url
    path('home/',home,name='home'),
    path('all_posts/',all_posts,name='all_posts')
    # path('individual_posts/', individual_posts, name='individual_posts'),
]