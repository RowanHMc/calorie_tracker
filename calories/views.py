from django.shortcuts import render
from .models import food

# Create your views here.
#function for home page
def home(request):

    if request.method == "POST":
        name = request.POST["name"]
        calories = request.POST["calories"]

        food.objects.create(
            name=name,
            calories=calories
        )
    return render(request, "index.html")