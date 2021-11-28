from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    is_admin = models.BooleanField(default=False)
    date_added = models.DateTimeField()
    date_edited = models.DateTimeField(null=True)
    
    def __repr__(self):
        return self.username


class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    work_names = models.CharField(max_length=20)
    users_to_groups = models.ManyToManyField(User)

    def __repr__(self):
        return self.name