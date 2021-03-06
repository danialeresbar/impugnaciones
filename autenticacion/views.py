from django import template
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from autenticacion.forms import LoginForm, SignUpForm


@login_required(login_url="/login/")
def index(request):
    context = dict()
    context['segment'] = 'index'
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


# def register_user(request):
#     msg = None
#     success = False
#
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             raw_password = form.cleaned_data.get("password1")
#             user = authenticate(username=username, password=raw_password)
#
#             msg = 'User created.'
#             success = True
#
#             # return redirect("/login/")
#
#         else:
#             msg = 'Form is not valid'
#     else:
#         form = SignUpForm()
#
#     return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


@login_required(login_url="/login/")
def index(request):
    context = dict()
    context['segment'] = 'index'
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]
        context['segment'] = load_template
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except Exception as e:
        print(f'Error: \n{e}')
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
