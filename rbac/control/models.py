from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    pwd = models.CharField(max_length=32)
    nickName = models.CharField(max_length=30)

class Role(models.Model):
    name = models.CharField(max_length=30)

class Url(models.Model):
    url = models.URLField()  

class user_role(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    url_id = models.ForeignKey(Url, on_delete=models.CASCADE)

class Op(models.Model):
    name = models.CharField(max_length=30)

class Resource(models.Model):
    name = models.CharField(max_length=30)
