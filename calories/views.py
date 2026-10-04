from django.shortcuts import render
from .models import Food

# Create your views here.
#function for home page
def home(request):

    if request.method == "POST":
        name = request.POST["name"]
        calories = request.POST["calories"]

        Food.objects.create(
            name=name,
            calories=calories
        )

    foods = Food.objects.all()


    return render(request, "index.html", {"foods":foods})