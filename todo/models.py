from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, default='-')
    completed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
