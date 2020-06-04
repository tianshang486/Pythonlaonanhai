from django.db import models

# Create your models here.

#书籍表
class Book(models.Model):
    title = models.CharField(max_length=16)
    price = models.FloatField()
    # pub_date = models.DateField()
    pub_date = models.DateTimeField()
    publish = models.CharField(max_length=16)

    def __str__(self):
        return self.title


















