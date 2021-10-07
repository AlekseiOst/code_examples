from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegistrationForm, UserEditForm


def login(request):
    title = 'вход'

    # login_form = UserLoginForm(data=request.POST)
    if request.method == 'POST':
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            # Получаем объект пользователя
            user = auth.authenticate(username=username, password=password)

            if user and user.is_active:
                # Прописываем пользователя в request. Залогинились!
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
        else:
            context = {'title': title,
                       'login_form': login_form}
            return render(request, 'authapp/login.html', context)
    else:
        login_form = UserLoginForm()
        context = {'title': title,
                   'login_form': login_form}
        return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def registration(request):
    title = 'регистрация'

    if request.method == 'POST':
        reg_form = UserRegistrationForm(request.POST, request.FILES)
        # reg_form = UserRegistrationForm(data=request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
        else:
            context = {'title': title,
                       'reg_form': reg_form}
            return render(request, 'authapp/registration.html', context)
    else:
        reg_form = UserRegistrationForm()
        context = {'title': title,
                   'reg_form': reg_form}
        return render(request, 'authapp/registration.html', context)


def edit(request):
    title = 'редактирование профиля'

    if request.method == 'POST':
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
        else:
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = UserEditForm(instance=request.user)
        context = {'title': title,
                   'edit_form': edit_form}
        return render(request, 'authapp/edit.html', context)
