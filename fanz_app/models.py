from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/')
    type = models.CharField(choices=(('image', 'Image'), ('video', 'Video')), max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.caption} - {self.type}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    rate = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)],null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender.username} to {self.recipient.username} - {self.created_at}'
    
    
class Subscription(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')
    start_date = models.DateTimeField(auto_now_add=True)
    # Add other details as needed

    def __str__(self):
        return f"{self.subscriber} subscribed to {self.creator}'s content"
