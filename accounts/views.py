from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.


def register(request):
    if request.method == 'POST':
        # Get Form
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        userName = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Check if passwords match
        if password != password2:
            messages.error(request, 'Passwords do not Match')
            return redirect('register')
        else:
            if User.objects.filter(username=userName).exists():
                messages.error(request, 'Username Already Taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email Already Used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=userName, password=password, email=email, first_name=firstName, last_name=lastName)
                    # Login after Register
                    auth.login(request, user)
                    messages.success(
                        request, 'Registration Successful!! You are now logged in')
                    return redirect('index')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        userName = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=userName, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Successfully Logged Out')
        return redirect('index')


def dashboard(request):
    #user.id = request.GET['user']
    print()
    contacts = Contact.objects.order_by(
        '-contact_date').filter(user_id=request.user.id)
    context = {'contacts': contacts}
    return render(request, 'accounts/dashboard.html', context)
