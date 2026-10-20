from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from  .forms import *
from django.utils import timezone


def home(request):
    
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {
        'form': form
    })

def user_login(request):
    form = LoginForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user:
                login(request, user)
                return redirect('home')
            else:
                form=LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def create_profile(request):

    profile = CalorieProfile.objects.filter(
        user=request.user
    ).first()

    if request.method == 'POST':
        form = CalorieProfileForm(
            request.POST,
            instance=profile
        )

        if form.is_valid():
            saved_profile = form.save(commit=False)
            saved_profile.user = request.user
            saved_profile.save()

            return redirect('dashboard')

    else:
        form = CalorieProfileForm(instance=profile)

    return render(request, 'profile_form.html', {
        'form': form
    })
    


@login_required
def dashboard(request):
    profile = CalorieProfile.objects.filter(
        user=request.user
    ).first()

    required_calories = 0

    if profile:
        if profile.gender.lower() == 'male':
            required_calories = (
                66.47
                + (13.75 * profile.weight)
                + (5.003 * profile.height)
                - (6.755 * profile.age)
            )

        elif profile.gender.lower() == 'female':
            required_calories = (
                655.1
                + (9.563 * profile.weight)
                + (1.850 * profile.height)
                - (4.676 * profile.age)
            )

    foods = FoodEntry.objects.filter(
        user=request.user,
        date=timezone.localdate()
    )

    consumed_calories = 0

    for food in foods:
        consumed_calories += food.calorie_consumed

    remaining_calories = required_calories - consumed_calories

    return render(request, 'dashboard.html', {
        'profile': profile,
        'required_calories': round(required_calories, 2),
        'foods': foods,
        'consumed_calories': round(consumed_calories, 2),
        'remaining_calories': round(remaining_calories, 2),
    })
    

@login_required
def add_food(request):
    if request.method == 'POST':
        form = FoodEntryForm(request.POST)

        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user
            food.save()

            return redirect('dashboard')
    else:
        form = FoodEntryForm()

    return render(request, 'add_food.html', {
        'form': form
    })
