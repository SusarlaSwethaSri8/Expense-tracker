from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    income = models.DecimalField(max_digits=10, decimal_places=2)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    savings_goal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
