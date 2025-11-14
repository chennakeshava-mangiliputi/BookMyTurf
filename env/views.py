from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Turf, Booking
from .forms import BookingForm, UserRegistrationForm
from django.contrib.auth import login, authenticate

def home(request):
    turfs = Turf.objects.filter(available=True)
    return render(request, 'home.html', {'turfs': turfs})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def book_turf(request, turf_id):
    turf = Turf.objects.get(id=turf_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.turf = turf
            booking.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'book_turf.html', {'form': form, 'turf': turf})
