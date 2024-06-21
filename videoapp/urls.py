from django.urls import path 
from django.contrib.auth import views as auth_views 
from . import views 
urlpatterns = [ 
    path('',views.login,name='login'),
    path('home/<int:pk>',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='videoapp/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='videoapp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='videoapp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='videoapp/password_reset_complete.html'), name='password_reset_complete'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('logout/',views.logout,name='logout')
]