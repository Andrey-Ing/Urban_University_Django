from django.shortcuts import render


# Create your views here.

def platform_view(request):
    return render(request, 'fourth_task/platform.html')


def games_view(request):
    context = {'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay2']}
    return render(request, 'fourth_task/games.html', context)


def cart_view(request):
    return render(request, 'fourth_task/cart.html')
