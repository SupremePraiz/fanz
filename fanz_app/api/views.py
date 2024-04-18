from rest_framework import generics


from fanz_app.models import Post, Like, Comment, Message
from .serializers import PostSerializer, LikeSerializer, CommentSerializer, MessageSerializer

'''this part handles posts accross users'''

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

'''this part handles likes accross users'''

class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = "LikeSerializer"

class LikeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = "LikeSerializer"
    

'''this part handles comments accross users'''

class CommentList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = CommentSerializer

class CommentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = CommentSerializer
    
'''this part handles messaging accross users'''

class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer