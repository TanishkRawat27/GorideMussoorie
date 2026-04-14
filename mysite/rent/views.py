from django.shortcuts import render
from .models import Booking
import requests


BOT_TOKEN = "PASTE_YOUR_TOKEN_HERE"
CHAT_ID = "PASTE_YOUR_CHAT_ID_HERE"


def site(request):
    return render(request, "index.html")


def booking(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        note = request.POST.get("note")

        car_quantity = request.POST.get("car_quantity") or 0
        scooty_quantity = request.POST.get("scooty_quantity") or 0

        Booking.objects.create(
            name=name,
            email=email,
            phone=phone,
            note=note,
            car_quantity=car_quantity,
            scooty_quantity=scooty_quantity
        )

        message = f"""
🚖 NEW BOOKING

Name: {name}
Email: {email}
Phone: {phone}

Cars: {car_quantity}
Scooty: {scooty_quantity}
Note: {note}
"""

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": message
        })

        return render(request, "bookings.html")

    return render(request, "bookings.html")


def pricing(request):
    return render(request, "pricing.html")


def bookcar(request):
    return render(request, "bookcar.html")


def bookscooty(request):
    return render(request, "bookscooty.html")


def leanmore(request):
    return render(request, 'leanmore.html')


def learnmore(request):
    return render(request, 'learnmore.html')