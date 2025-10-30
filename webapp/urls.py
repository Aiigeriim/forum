from django.urls import path

from webapp.views import CreateTopic, TopicsList, TopicDetail, AnswerAdd, AnswerUpdate, AnswerDelete

app_name = "webapp"

urlpatterns = [
    path('', TopicsList.as_view(), name="topics_list"),
    path('topic/add/', CreateTopic.as_view(), name="topic_add"),
    path('topic/<int:pk>/', TopicDetail.as_view(), name="topic_view"),
    path('topic/<int:pk>/add-answer/', AnswerAdd.as_view(), name="add_answer"),
    path('answer/<int:pk>/update/', AnswerUpdate.as_view(), name="update_answer"),
    path('answer/<int:pk>/delete/', AnswerDelete.as_view(), name="delete_answer"),
    #
    # path('post/<int:pk>/comments/add/', CommentCreate.as_view(), name="comment_add"),
    # path('topic/<int:pk>/answer/<int:pk>/update/', AnswerUpdate.as_view(), name="update_answer"),

]