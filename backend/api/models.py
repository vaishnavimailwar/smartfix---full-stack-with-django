from django.db import models
from django.contrib.auth.models import User


class RepairRequest(models.Model):

    # ✅ Choices
    URGENCY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted')
    ]

    # ✅ Customer Details
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    # ✅ Vehicle Details
    vehicle = models.CharField(max_length=50)
    reg_no = models.CharField(max_length=30, blank=True)

    # ✅ Location
    address = models.TextField(blank=True)
    latitude = models.CharField(max_length=20, blank=True)
    longitude = models.CharField(max_length=20, blank=True)

    # ✅ Problem
    problem = models.TextField()
    urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES)

    # 🔥 Mechanic (AUTO ASSIGNED)
    mechanic = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # ✅ Status
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    # ✅ Time
    timestamp = models.DateTimeField(auto_now_add=True)

    # ✅ Display
    def __str__(self):
        mech = self.mechanic.username if self.mechanic else "No Mechanic"
        return f"#{self.id} - {self.name} | {self.status} | {mech}"