from django.db import models

class don(models.Model):
    name=models.CharField( max_length=50)
    contact=models.IntegerField()
    class Meta:
        db_table='don'