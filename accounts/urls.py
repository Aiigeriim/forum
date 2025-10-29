from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accounts.views import RegisterView

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='registration'),
    # path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    # path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='profile_update'),
    # path('profile/<int:pk>/follow', FollowView.as_view(), name='follow'),
    # path('profile/<int:pk>/followers', FollowersView.as_view(), name='followers'),
    # path('profile/<int:pk>/followings', FollowingView.as_view(), name='followings'),
    # path('users/', UserListView.as_view(), name='users'),


]