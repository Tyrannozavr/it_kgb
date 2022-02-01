from django.shortcuts import render
from application.models import Users
import re


def valid_number(tel):
    pattern = re.compile(r'\+?\d{9,15}')
    return bool(pattern.match(tel))

def index(request):
    if request.POST:
        name = request.POST['Name']
        email = request.POST['Email']
        tel = request.POST['tel']
        if valid_number(tel):
            Users.objects.create(name=name, email=email, phone_number=tel)
        else:
            message = 'Недопустимый формат номера'
            return render(request, 'index.html', {'message': message})
    return render(request, 'index.html')



