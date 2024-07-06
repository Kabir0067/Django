from django.db import models

DUE = (
    ('1', 'Monday'),
    ('2', 'Tuesday'),
    ('3', 'Wednesday'),
    ('4', 'Thursday'),
    ('5', 'Friday'),
    ('6', 'Saturday'),
    ('7', 'Sunday'),
)

class CustomUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)  
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Tasks(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=230)
    due_date = models.CharField(max_length=50, choices=DUE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
