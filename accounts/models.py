from django.db import models

class ServiceProvider(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    service = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    address = models.TextField()

    profile_picture = models.ImageField(
        upload_to='providers/profile/',
        null=True,
        blank=True
    )

    id_proof = models.FileField(
        upload_to='providers/idproof/',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

# signup form model
class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email