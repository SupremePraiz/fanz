from rest_framework import serializers
from django.contrib.auth.models import User
from fanz_app.models import Post, Like, Comment, Message


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"

# class PostSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
   
#     class Meta:
#         model = Post
#         fields = "__all__"


# class LikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Like
#         fields = "__all__"

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = "__all__"

# class MessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Message
#         fields = "__all__"





class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = "__all__"
        
class LikeSerializer(serializers.ModelSerializer):
    post = PostSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = "__all__"
        
class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(many=True, read_only=True)
    
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