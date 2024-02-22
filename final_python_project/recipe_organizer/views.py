from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect

# Create your views here.
def recipes(request):
    if request.method=="POST":
        data=request.POST
        recipe_name=data.get("recipe_name")
        recipe_text=data.get("recipe_text")
        recipe_picture=request.FILES.get("recipe_picture")
        
        recipe.objects.create(
            recipe_name=recipe_name,
            recipe_picture=recipe_picture,
            recipe_text= recipe_text

            )
    datalist=recipe.objects.all()
    get_data={'recipes':datalist}
    return render(request,'recipes.html',get_data)

def delete_recipe(request, id):
    recipe_instance = recipe.objects.get(id=id)
    recipe_instance.delete()
    return redirect('recipes')