from django.db import models


# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100, default=" ")
    phone = models.CharField(max_length=60, default="")

    textarea = models.CharField(max_length=10000)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.name} " - " {self.email}'

