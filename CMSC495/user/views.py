from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm


@login_required
def profile(request):
    context = {
        "welcome": "Welcome to your dashboard"
    }
    return render(request, 'user/profile.html', context=context)


def register(request):
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
