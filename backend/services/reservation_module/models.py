# import os
# from django.db import models
#
#
# class UserReservation(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.EmailField()
#     one = '1'
#     two = '2'
#     three = '3'
#     four = '4'
#     five = '5'
#     people_choices = ((one, 'one person'), (two, 'two people'), (three, 'three people'),
#                       (four, 'four people'), (five, 'five  people'))
#     people = models.CharField(max_length=1, choices=people_choices, default=one)
#     date = models.DateField()
#     time = models.TimeField()
#     # pending = "pending"
#     # confirmed = "confirmed"
#     # status_choices = ((pending, "pending"), (confirmed, "confirmed"))
#     # status = models.CharField(
#     #     max_length=10, choices=status_choices, default=pending)
#     comment = models.TextField(blank=True)
#
#     def __str__(self):
#         return self.first_name
