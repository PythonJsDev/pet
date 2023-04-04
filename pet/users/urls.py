from django.urls import path
from .views import profile_view, UserUpdateView, UserDeleteView

urlpatterns = [
    path('profile/', profile_view, name='account_profile'),
    path(
        '<int:pk>/update/',
        UserUpdateView.as_view(template_name='account/update.html'),
        name='account_update',
    ),
    path(
        '<int:pk>/delete/',
        UserDeleteView.as_view(template_name='account/delete.html'),
        name='account_delete',
    ),
]
