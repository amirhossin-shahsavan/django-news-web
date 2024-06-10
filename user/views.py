from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from .forms import RegisterForm, ProfileForm,LoginForm

class RegisterView(View):
    user_form_class = RegisterForm
    profile_form_class = ProfileForm
    template_name = 'register/index.html'

    def get(self, request, *args, **kwargs):
        user_form = self.user_form_class()
        profile_form = self.profile_form_class()
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request, *args, **kwargs):
        user_form = self.user_form_class(request.POST)
        profile_form = self.profile_form_class(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')  # Ensure you have a named URL pattern for login

        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})




class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login/index.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True

        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.get_form()})