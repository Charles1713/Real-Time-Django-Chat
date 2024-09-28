from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LogInForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
