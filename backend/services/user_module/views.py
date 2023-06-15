from django.http import HttpResponseNotFound, HttpResponse

from services.user_module import admin
from services.user_module.forms import RegistrationForm, AuthForm, ProfileForm, ReservationForm
from django.contrib.auth import authenticate, login, get_user_model

from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from django.db import models

from settings import SITE_URL
from utils.send_email.send_email import send_email

User = get_user_model()


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(email=form.data['email'],
                                            username=form.data['username'],
                                            password=form.data['password'])
            user.first_name = form.data['first_name']
            user.last_name = form.data['last_name']

            user.save()
        else:
            print(form)

        return redirect('auth')
    else:
        form = RegistrationForm()

        return render(request, 'registration.html', context={'form': form})


def auth(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.data['username'],
                                password=form.data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form = AuthForm()
                return render(request, 'auth.html', context={'form': form, 'SITE_URL': SITE_URL})
    else:
        form = AuthForm()
        return render(request, 'auth.html', context={'form': form, 'SITE_URL': SITE_URL})


def profile(request):
    if not request.user.is_authenticated:
        return redirect('auth')

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = request.user

            user.first_name = form.data['first_name']
            user.last_name = form.data['last_name']

            if not User.objects.filter(email=form.data['email']).exists():
                user.email = form.data['email']

            if not User.objects.filter(username=form.data['username']).exists():
                user.username = form.data['username']

            if form.data['password_old'] \
                    and form.data['password_new'] \
                    and user.check_password(form.data['password_old']):
                user.password = make_password(form.data['password_new'])

            user.save()

            return redirect('profile')
        else:
            return render(request, 'profile.html', context={'form': form})
    else:
        form = ProfileForm(data={'first_name': request.user.first_name,
                                 'last_name': request.user.last_name,
                                 'username': request.user.username,
                                 'email': request.user.email})

        return render(request, 'profile.html', context={'form': form})


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reserv = User.objects.create_reservation(email=form.data['email'],
                                                     username=form.data['username'],
                                                     password=form.data['password'],
                                                     people=form.data['people'],
                                                     date=form.data['date'],
                                                     time=form.data['time'])
            reserv.first_name = form.data['first_name']
            reserv.last_name = form.data['last_name']

            reserv.save()
            return HttpResponse("Table booked successfully!")
        else:
            return HttpResponse("Please fill in all the required fields.")
    else:
        form = ReservationForm()
        return render(request, 'reservation.html', {'form': form})

# class NewReservation(CreateView):
#     template_name = "reservation.html"
#     form_class = ReservationForm
#
#     def form_valid(self, form):
#         new = form.save(commit=False)
#         new.save()
#         # sends a flash message to the user
#         messages.success(
#             self.request,
#             "you have successfully booked a new")
#
#
# def reservation(request):
#     if request.method == 'POST':
#         table_number = request.POST.get('table_number')
#         reservation_date = request.POST.get('reservation_date')
#
#         # Валідація даних
#         if not table_number or not reservation_date:
#             return HttpResponse("Please fill in all the required fields.")
#
#         # Збереження даних в базу даних або інша обробка
#         # ...
#
#         return HttpResponse("Table booked successfully!")
#
#         # return render(request, 'registration.html', context={'form': form})

