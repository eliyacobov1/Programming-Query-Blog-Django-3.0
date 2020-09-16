from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, LogInForm


def log_in_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.POST:
        my_form = LogInForm(request.POST)
        if my_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")

    else:
        my_form = LogInForm()

    return render(request, "log_in.html", {"form": my_form,
                                           "page": "home"})


def register_view(request):
    if request.user.is_authenticated:
        return redirect("/home")

    if request.POST:
        my_form = UserRegistrationForm(request.POST)

        if my_form.is_valid():
            my_form.save()
            email = my_form.cleaned_data.get('email')
            raw_password = my_form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)

            redirected = True  # redirect to success page
            return success_registration_view(request, redirected)
    else:
        my_form = UserRegistrationForm()

    return render(request, "register_form.html", {"form": my_form,
                                                  "page": "home"})


def success_registration_view(request, redirected_page=False):
    if not redirected_page:  # If not redirected from register page
        return redirect('/home')

    return render(request, "success_registration.html", {"page": "home"})


def logout_view(request):
    logout(request)
    return redirect('/home')
