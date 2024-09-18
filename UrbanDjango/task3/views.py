from django.shortcuts import render


# Create your views here.

def platform_view(request):
    return render(request, 'third_task/platform.html')


def aircraft_view(request):
    context = {
        'russian': 'ОКБ С.В. Ильюшина',
        'european': 'Airbus S.A.S.',
        'american': 'Boeing',
    }
    return render(request, 'third_task/games.html', context)


def cars_view(request):
    return render(request, 'third_task/cart.html')
