from django.urls import path

from webapp.views import CreateTopic, TopicsList, TopicDetail, AnswerAdd

app_name = "webapp"

urlpatterns = [
    path('topic/add/', CreateTopic.as_view(), name="topic_add"),
    path('topics/list/', TopicsList.as_view(), name="topics_list"),
    path('topic/<int:pk>/', TopicDetail.as_view(), name="topic_view"),
    path('topic/<int:pk>/add-answer/', AnswerAdd.as_view(), name="add_answer"),
    # path('post/<int:pk>/delete/', PostDelete.as_view(), name="post_delete"),
    # path('post/<int:pk>/like/', PostLike.as_view(), name="post_like"),
    #
    # path('post/<int:pk>/comments/add/', CommentCreate.as_view(), name="comment_add"),
    # path('post/<int:pk>/comments/<int:pk>/update/', CommentUpdate.as_view(), name="comment_update"),

]