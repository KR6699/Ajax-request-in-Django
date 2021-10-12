from django.db import models

# Create your models here.
class Post(models.Model):
    heading = models.CharField(max_length=50)
    data = models.TextField()

    def __str__(self):
        return self.heading

class Likes(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE)

    