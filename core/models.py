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
    
    def __str__(self):
        return self.title
    
class Comment(BaseTimestampModel):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'