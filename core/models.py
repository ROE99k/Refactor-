from django.db import models

# Reusable Mixin
class BaseTimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # This prevents creating a separate table
class Post(BaseTimestampModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
