from django.db import models

# models

class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True) #takes timestamp on every update
    created = models.DateTimeField(auto_now_add=True) #takes timestamp only when created

    def __str__(self):
        return self.body[0:50] # return only first 50 chars
