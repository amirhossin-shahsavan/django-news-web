# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('user/login')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
    return render(request, 'register/index.html', {'user_form': user_form, 'profile_form': profile_form})




# @login_required
def login(request):
    return render(request, "login/index.html", {})



