from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from image.models import Image

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("image_list_view")

class ImageListView(ListView):
    model = Image

class ImageCreateView(CreateView):
    model = Image
    fields = ('picture', 'title', 'description')
    success_url = reverse_lazy('image_list_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

class ImageUpdateView(UpdateView):
    model = Image
    fields = ('picture', 'title', 'description')
    success_url = reverse_lazy('image_list_view')
