from django.db import models

# Create your models here.
class Products(models.Model):
    """
    Creating the Table in the database with name Productss

    :param:
        name: string
        price: number
        description: string
        image: string

    """
    name = models.CharField(max_length=20)
    price =  models.IntegerField()
    description = models.TextField()
    image= models.ImageField(upload_to='pics')

