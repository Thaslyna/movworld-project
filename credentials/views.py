from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        uname = request.POST['userName']
        f_name = request.POST['firstName']
        l_name = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['psw']
        cpassword = request.POST['psw-repeat']

        if password == cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "username exists")
                return redirect('credential:signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email exists")
                return redirect('credential:signup')
            else:
                create = User.objects.create_user(username=uname, first_name=f_name, last_name=l_name, email=email,
                                                  password=password)
                create.save()
                print("user created")
                messages.success(request, 'User created successfully')
                return redirect("credential:signin")
        else:
            messages.info(request, "password not matching")
            return redirect('credential:signup')
    return render(request, "signup.html")


def signin(request):
    if request.method == "POST":
        u_n = request.POST.get("username", '')
        passw = request.POST.get("password", '')
        check = auth.authenticate(username=u_n, password=passw)
        if check is not None:
            auth.login(request, check)
            messages.info(request, "Welcome to Movworld, we are thrilled to have you join our community and share your love for movies with us.")
            return redirect('/')
        else:
            messages.warning(request, "username or password is invalid")
            return redirect("credential:signin")
    return render(request, "signin.html")


def signout(request):
    auth.logout(request)
    return redirect('/')


def user_det(request, u_id):
    user_d = User.objects.get(id=u_id)
    return render(request, 'user_det.html', {'user': user_d})
