from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import chat_view

urlpatterns = [
    path('', chat_view, name='chat'),  # Main chat view
    path('login/', LoginView.as_view(template_name='chat/login.html'), name='login'),  # Login page
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),  # Logout page
]
