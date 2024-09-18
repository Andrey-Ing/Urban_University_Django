from django.shortcuts import render
from .forms import UserRegister

# Create your views here.

users = ['Andrey', 'admin', 'user']  # псевдо-список users уже существующих пользователей
ACCEPTABLE_AGE = 18


def data_verification(username, password, repeat_password, age):
    answer = {}
    if username in users:
        answer['error'] = 'Пользователь уже существует'
    elif password != repeat_password:
        answer['error'] = 'Пароли не совпадают'
    elif age < ACCEPTABLE_AGE:
        answer['error'] = f'Вы должны быть старше {ACCEPTABLE_AGE}'
    else:
        answer['success'] = f'Приветствуем, {username}!'

    return answer


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]

            info = data_verification(username, password, repeat_password, age)
            if 'success' in info:
                users.append(username)
        else:
            form = UserRegister()
            info['form'] = form
        return render(request, 'fifth_task/registration_page.html', context=info)

    return render(request, 'fifth_task/registration_page.html', context=info)  # если это GET запрос, то выводим форму


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = int(request.POST.get("age"))

        info = data_verification(username, password, repeat_password, age)
        if 'success' in info:
            users.append(username)

        return render(request, 'fifth_task/registration_page.html', context=info)

    return render(request, 'fifth_task/registration_page.html', context=info)  # если это GET запрос, то выводим форму
