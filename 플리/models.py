from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=20)
    pw = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} {self.pw} {self.created_at} {self.updated_at}'