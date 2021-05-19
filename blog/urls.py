from django.contrib import admin
from django.urls import path
from blog.views import *
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from config import settings


urlpatterns = [
    path('password-reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset_form'),
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
    path('add-category/', AddCategoryView.as_view(), name='add_category'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('category/<str:cats>/', CategoryView, name='categories'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('post/<int:pk>/comment', BlogCommentView.as_view(), name='comment'),
    path('', BlogListView.as_view(), name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
