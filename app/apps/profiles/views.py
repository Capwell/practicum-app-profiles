from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.detail import DetailView

from .forms import SignUpForm


class RegistrationView(FormView):
    template_name = 'profiles/registration.html'
    form_class = SignUpForm
    success_url = reverse_lazy('profiles:profile')

    def form_valid(self, form):
        email = self.request.POST['email']
        password = self.request.POST['password1']
        form.save()
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return super(RegistrationView, self).form_valid(form)


class UserView(DetailView):
    template_name = 'profiles/profile.html'

    def get_object(self):
        return self.request.user
