from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm


@login_required
def profileView(request):
    context = {
        "welcome": "Welcome to your dashboard"
    }
    return render(request, 'user/profile.html', context=context)


def registerView(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'user/profile.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'user/register.html', context=context)


@login_required
def editView(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'user/edit.html', context=context)
