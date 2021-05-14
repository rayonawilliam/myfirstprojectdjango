from django.db import models

# Create your models here.
class Advisor(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    advisor_id=models.IntegerField()

    def __str__(self):
        return self.firstname()




class registeruser(models.Model):

    username= models.CharField(max_length=10)

    email=models.CharField(max_length=10)
    password=models.IntegerField()

    def __str__(self):
        return self.username()


class bookadvisor(models.Model):

    advisor_id=models.IntegerField()
    time=models.DateTimeField()

    def __str__(self):
        return int( self.advisor_id)
