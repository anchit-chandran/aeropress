from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Recipe
from .forms import RecipeForm

# Create your views here.


def home(response):

    if response.method == 'POST':
        print(response.POST)
        form = RecipeForm(response.POST)
        if form.is_valid():
            f = Recipe(
                coffee_g=form.cleaned_data['coffee_g'],
                water_brew_ml=form.cleaned_data['water_brew_ml'],
                brew_time_s=form.cleaned_data['brew_time_s'],
                milk_ml=form.cleaned_data['milk_ml'],
                extra_water_ml=form.cleaned_data['extra_water_ml'],
                nausea=form.cleaned_data['nausea'],
                rating=form.cleaned_data['rating'],
            )
            f.save()
            return HttpResponseRedirect('/')
    else:
        form = RecipeForm(initial={
            'coffee_g': 0,
            'water_brew_ml' : 0,
            'brew_time_s' : 0,
            'milk_ml' : 0,
            'extra_water_ml' : 0,
            'rating' : 0,
        })
    rs = Recipe.objects.all()
    return render(response, 'aeropress/base.html', {'rs': rs, 'form': form})
