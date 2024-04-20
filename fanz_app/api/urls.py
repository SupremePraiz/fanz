from django.urls import path
from . views import PostList, PostDetail, CommentList, CommentDetails,CommentCreate, MessageList, MessageDetails

urlpatterns = [
   path("post/",PostList.as_view(),name="post_list"),
   
   path("post/<int:pk>/detail/",PostDetail.as_view(),name="post_detials"),
   
   path("post/<int:pk>/comment/",CommentList.as_view(),name="comment_list"),
   
   path("post/<int:pk>/comment-create/",CommentCreate.as_view(),name="comment_create"),
   
   path("comment/<int:pk>/detail/",CommentDetails.as_view(),name="comment_detials"),
   
   path("message/",MessageList.as_view(),name="message_list"),
   path("message/<int:pk>/detail/",MessageDetails.as_view(),name="message_ details"),
]
