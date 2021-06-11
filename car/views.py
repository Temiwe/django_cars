from django.shortcuts import render, get_object_or_404
from car.models import Car


# Create your views here.
def car_view(request, id=None):
    context = {}
    if id:
        car = get_object_or_404(Car, pk=id)
        context.update({
            "car": car
        })
    context.update(
        {"cars": Car.objects.all()}
    )
    return render(request, 'car.html', context)
