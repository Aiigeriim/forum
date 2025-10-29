from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from accounts.forms import MyUserCreationForm


class RegisterView(CreateView):
    template_name = "accounts/user_create.html"
    model = get_user_model()
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse('webapp:topics_list'))


