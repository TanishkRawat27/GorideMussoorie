from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    car_quantity = models.PositiveIntegerField(default=0)
    scooty_quantity = models.PositiveIntegerField(default=0)

    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name