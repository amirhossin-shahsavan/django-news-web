from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def login(request):
    return render(request, "login/index.html", {})

def register(request):
    return render(request, "register/index.html", {})

# def authView(request):
#     if request.method == "POST":
#   form = UserCreationForm(request.POST or None)
#     if form.is_valid():
#    form.save()
#     return redirect("login/index.html")
#  else:
#   form = UserCreationForm()
#     return render(request,"register/index.html",{"form":form})

    