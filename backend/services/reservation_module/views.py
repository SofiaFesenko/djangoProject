# from django.http import HttpResponse
# from django.shortcuts import render
#
# from services.reservation_module.forms import ReservationForm
#
#
# def reservation(request):
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             reserv = ReservationForm.create_reservation(email=form.data['email'],
#                                                      username=form.data['username'],
#                                                      password=form.data['password'],
#                                                      people=form.data['people'],
#                                                      date=form.data['date'],
#                                                      time=form.data['time'])
#             reserv.first_name = form.data['first_name']
#             reserv.last_name = form.data['last_name']
#
#             reserv.save()
#             return HttpResponse("Table booked successfully!")
#         else:
#             return HttpResponse("Please fill in all the required fields.")
#     else:
#         form = ReservationForm()
#         return render(request, 'index', {'form': form})
