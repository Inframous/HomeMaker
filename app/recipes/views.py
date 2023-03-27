from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Recipe
from .forms import RecipeForm, SearchForm
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Q
from .categories import CATLIST_SETS, CATLIST_DICT

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        last_five_entries = Recipe.objects.all().order_by('-id')[:5]
        return render(request, 'home.html', {'last_five_entries': last_five_entries})
    else:
        return redirect('login')

def show_db(request):
    if request.user.is_authenticated:
        all_recipes = Recipe.objects.all()
        return render(request, 'show_db.html', {'all_recipes': all_recipes})
    else:
        return redirect('login')

def show_recipe(request, recipe_id):
    if request.user.is_authenticated:
        recipe = Recipe.objects.get(pk=recipe_id)
        ing_list = recipe.parse_ingredients()
        return render(request, 'show_recipe.html', {'recipe': recipe, 'catlist': CATLIST_SETS, 'ing_list': ing_list})
    else:
        return redirect('login')


def search_db(request):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            title = request.POST.get('title', '')
            mealcat = request.POST.get('mealcat', '')

            query = Q()
            for search_term in [title, mealcat]:
                if search_term:
                    query |= Q(title__icontains=search_term) | Q(mealcat__icontains=search_term)

            searched_recipe = Recipe.objects.filter(query)
            
            if mealcat != '':
                search_term = f'{title} {CATLIST_DICT[mealcat]}'.strip()
            form = SearchForm()
            context = {'searched_recipe': searched_recipe, 'search_term': search_term, 'form': form}
            
            return render(request, 'search_db.html', context)
        else:
            form = SearchForm()
            return render(request, 'search_db.html', {'form': form})
    else:
        return redirect('login')


def new_recipe(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                print(form.files)
                form.save()
                form = RecipeForm()
                messages.success(request, "המתכון נשמר בהצלחה!")
                return render(request, 'new_recipe.html', {'form': form})
            else:
                return render(request, 'new_recipe.html', {'form': form})
        if request.method == 'GET':
            form = RecipeForm()
            return render(request, 'new_recipe.html', {'form': form})
    else:
        return redirect('login')

def edit_recipe(request, recipe_id):
    if request.user.is_authenticated:
        rec_id = recipe_id
        if request.method == 'GET':
            recipe = Recipe.objects.get(pk=recipe_id)
            form = RecipeForm(request.POST or None, instance=recipe,initial={"mealcat": recipe.get_cat_list(),"mealtype": recipe.get_type_list() })
            return render(request, 'edit_recipe.html', {'recipe': recipe, 'form': form})

        elif request.method == 'POST':
            recipe = Recipe.objects.get(pk=rec_id)
            form = RecipeForm(request.POST, request.FILES, instance=recipe)
            if form.is_valid():
                form = RecipeForm(request.POST, request.FILES, instance=recipe)
                form.save()
                messages.success(request, "המתכון עודכן בהצלחה!")
                return redirect('show_db')
            else:
                print(request.POST)
                print("Form not valid")
    else:
        return redirect('login')
    

def delete_recipe(request, recipe_id):
    if request.user.is_authenticated:
        if not Recipe.objects.filter(id=recipe_id).exists():
            messages.error(request, "שגיאה: המתכון לא קיים")
            return render(request, 'home.html', {})
        else:
            recipe = Recipe.objects.get(id=recipe_id) # we need this for both GET and POSt
            
            if request.method == 'GET':
                return render(request, 'delete_recipe.html', {'recipe':recipe})

            elif request.method == 'POST':
                # delete the band from the database
                recipe.delete()
                # redirect to the bands list
                return redirect('show_db')
    else:
        return redirect('login')
    # no need for an `else` here. If it's a GET request, just continue

...