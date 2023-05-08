from django.db import models

# Create your models here.
class User(models.Model):
    name = models.Charfield(max_length = 40)

    @staticmethod
    def get_all_users():
        return User.objects.all()
    
    def__str__(self):
    return self.name


