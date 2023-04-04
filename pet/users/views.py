# from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView

from .forms import UserUpdateForm

User = get_user_model()


@login_required
def profile_view(request):
    return render(request, 'account/profile.html')


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('account_signup')
