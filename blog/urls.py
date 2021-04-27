from django.contrib import admin
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from blog.views import SignUpView, AdminLogin
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
         ),
         name='password_reset_complete'),
    path('change-password/', auth_views.PasswordChangeView.as_view(success_url='/home'),
         name='change_password'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('login/', AdminLogin.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('blog/<int:_id>', BlogDetailView, name='blog'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]
