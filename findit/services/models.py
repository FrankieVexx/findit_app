from django.db import models


# Create your models here.

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    service_description = models.TextField(max_length=10000)
    service_pub_date = models.DateTimeField(auto_created=True)



