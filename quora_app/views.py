# views.py
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .forms import *

# Auth views 

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')

            if User.objects.filter(email=email).exists():
                form.add_error('email', 'Email already exists')
                return render(request, 'signup.html', {'form': form})


            # when the user register for the first time otp should be sent to the mail and the below is the otp variable which generates the otp of 6 digits 
            
            user = User.objects.create_user(
                username=username,
                email=email,
                password=form.cleaned_data.get('password')
            )
            return redirect('signin')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if (email):
                try:
                    user = User.objects.get(email=email)
                except User.DoesNotExist:
                    form.add_error('email', 'Incorrect email or password')
                    return render(request, 'signin.html', {'form': form})
            else:
                try:
                    user = User.objects.get(email=email)
                except User.DoesNotExist:
                    form.add_error('email', 'Incorrect email or password')
                    return render(request, 'signin.html', {'form': form})
            
            # The check_password method is basically used to decode the hashed password that is saved in the table

            if not check_password(password, user.password):
                form.add_error('email', 'Incorrect email or password')
                return render(request, 'signin.html', {'form': form})

            login(request, user)


            user.save()

            return redirect('home')

    else:
        form = SignInForm()

    return render(request, 'signin.html', {'form': form})



# logout functionality 

def logout_user(request):
    if request.user.is_authenticated:
        user = request.user
        user.save()
        logout(request)
    return redirect('signin')



