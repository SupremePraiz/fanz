from django.urls import path
from . views import PostList, PostDetail, CommentList, CommentDetails, LikeList, LikeDetails, MessageList, MessageDetails

urlpatterns = [
   path("post/",PostList.as_view(),name="post_list"),
   path("post/<int:pk>/detail/",PostList.as_view(),name="post_detials"),
   
   path("like/",LikeList.as_view(),name="like_list"),
   path("like/<int:pk>/detail/",LikeDetails.as_view(),name="like_detials"),
   
   path("comment/",CommentList.as_view(),name="comment_list"),
   path("comment/<int:pk>/",CommentDetails.as_view(),name="comment_detials"),
   
   path("message/",MessageList.as_view(),name="message_list"),
   path("message/<int:pk>/detail/",MessageDetails.as_view(),name="message_ details"),
]
