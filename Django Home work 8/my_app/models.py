from django.db import models

COLOR = (
    ('RED', 'Red'),
    ('BLACK', 'Black'),
    ('GREEN', 'Green'),
    ('GREY', 'Grey'),
    ('YELLOW', 'Yellow'),
    ('WHITE', 'White'),
)

class Ctegotiya(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50,choices=COLOR)
    quantity = models.IntegerField()
    catigoriya = models.ForeignKey(Ctegotiya, on_delete=models.CASCADE)
    

    
    