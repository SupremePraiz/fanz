from rest_framework import serializers
from django.contrib.auth.models import User
from fanz_app.models import Post, Comment, Message, Subscription


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Comment
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Post
        fields = "__all__"
    
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        
        
class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = "__all__"
        
class SubscriptionSerializer(serializers.ModelSerializer):
    subscriber = serializers.StringRelatedField(read_only=True)
    creator = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Subscription
        fields = "__all__"