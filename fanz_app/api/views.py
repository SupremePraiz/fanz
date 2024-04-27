from rest_framework import generics
from django.contrib.auth.models import User

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from fanz_app.models import Post, Comment, Message, Subscription
from .serializers import PostSerializer,CommentSerializer, MessageSerializer, SubscriptionSerializer

'''this part handles posts accross users'''
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class =PostSerializer

# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsOwnerOrReadOnly]
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

'''this part handles comments accross users'''

class CommentList(generics.ListAPIView):
   
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(post=pk)
    
class CommentCreate(generics.CreateAPIView):

    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        serializer.save(post=post)

class CommentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
'''this part handles messaging accross users'''

    
class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    
'''this part handles Subscription accross users'''

class SubscriptionList(generics.ListAPIView):
  
    serializer_class = SubscriptionSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Subscription.objects.filter(creator=pk)
    
class SubscriptionCreate(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    
class SubscriptionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer