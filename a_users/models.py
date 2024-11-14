from django.templatetags.static import static
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    display_name = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    @property
    def display_name_or_username(self):
        return self.display_name if self.display_name else self.user.username

    @property
    def profile_image(self):
        return self.image.url if self.image else static('a_users/default.jpg')
