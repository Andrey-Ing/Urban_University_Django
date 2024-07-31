from django.shortcuts import render


# Create your views here.

def platform_view(request):
    return render(request, 'third_task/platform.html')


def aircraft_view(request):
    context = {
        'Россия': 'ОКБ С.В. Ильюшина',
        'Европейский_Союз': 'Airbus S.A.S.',
        'США': 'Boeing',
    }
    return render(request, 'third_task/aircraft.html', context)


def cars_view(request):
    return render(request, 'third_task/cars.html')
