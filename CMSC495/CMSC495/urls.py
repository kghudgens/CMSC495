from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from user import views as user_views

urlpatterns = [
    # Path is empty because it is the home page
    path("", include('bug_tracker.urls')),
    path("accounts/", include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path("accounts/login",
         auth_views.LoginView.as_view(template_name="user/login.html"), name="login"),
    path("accounts/logout",
         auth_views.LogoutView.as_view(template_name="user/logout.html"), name="logout"),
    path("accounts/profile", user_views.profileView, name='profile'),
    path("accounts/edit", user_views.editView, name='edit'),
    path("accounts/register", user_views.registerView, name='register')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
