from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    if request.method == 'POST':
        # register user
        messages.error(request, "Test error message")
        # get form values
        first_name = request.POST['first_name'];
        last_name = request.POST['last_name'];
        username = request.POST['username'];
        email = request.POST['email'];
        password = request.POST['password'];
        password2 = request.POST['password2'];

        # validation
        if password ==password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "username already exists")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "email already exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,
                    email=email,password=password)
                    # login user
                    # auth.login(request, user)
                    # messages.success(request, "you are registered successfully");
                    # return redirect('dashboard');
                    user.save();
                    messages.success(request, "you are registered  successfully")
                    return redirect('login')
        else:
            messages.error(request, "passwords does not match")
            return redirect('register')
        # return redirect('register');
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # login user
        username = request.POST['username'];
        password = request.POST['password'];

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user);
            messages.success(request, "You are logged in successfully")
            return redirect('dashboard')
        else:
            messages.error(request, "invalid username of password")
        return redirect('login');
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "you are now logged out")
        return redirect('index')
    else:
        return redirect('dashboard');

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)
    contex ={
        'contacts':user_contacts
    }
    return render(request, 'accounts/dashboard.html', contex)
