from django.db import models

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('haircut', 'Haircut'),
        ('coloring', 'Coloring'),
        ('styling', 'Styling'),
    ]

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    notes = models.TextField(blank=True, null=True)
    date_preference = models.DateField()
    time_preference = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.service_type} - {self.date_preference} {self.time_preference}'