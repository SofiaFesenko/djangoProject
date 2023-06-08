from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')


class ProfileForm(forms.ModelForm):
    password_old = forms.CharField(required=False)
    password_new = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')


class AuthForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class ReservationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    # date_reserved = forms.DateField(widget=forms.TextInput(attrs={}), required=True,)
    # email = forms.EmailField(widget=forms.TextInput(attrs={'id': 'reservation_email', 'placeholder': "Your Email"}))
    # time = forms.TimeField(widget=forms.TextInput(attrs={'id': 'reservation_time', 'placeholder': "Expected time"}))
    #
    # comment = forms.CharField(widget=forms.Textarea(attrs={'col': '30', 'rows': '10', 'placeholder': 'comment'}))
    # phone = forms.CharField(widget=forms.TextInput( attrs={'placeholder': 'Phone No start with +234',
    #                                                        'id': 'reservation_phone', }), required=True,)
