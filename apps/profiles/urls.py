from django.urls import path
from apps.profiles import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    #AUTH URLS
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(template_name = "auth/signin.html"), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
