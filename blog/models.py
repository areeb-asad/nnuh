from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    post_date = models.DateTimeField('date published')
    content = models.CharField(max_length=200)
    pub_user = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Comments(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    Fname = models.CharField(max_length=200)
    Lname = models.CharField(max_length=200)
    Comment = models.CharField(max_length=500)
    Email = models.CharField(max_length=200)