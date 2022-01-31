from django.shortcuts import render
from application.models import Users


def index(request):
    if request.POST:
        name = request.POST['Name']
        email = request.POST['Email']
        tel = request.POST['tel']
        Users.objects.create(name=name, email=email, phone_number=tel)
    return render(request, 'index.html')