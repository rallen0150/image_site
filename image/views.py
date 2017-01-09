from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from image.models import Image, Comment, Category

class IndexView(TemplateView):
    template_name = 'index.html'

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("index_view")

class CategoryListView(ListView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    fields = ('title', )
    success_url = reverse_lazy('category_list_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

class CategoryDetailView(DetailView):
    model = Category
    # paginate_by = 9
    # contact_list = Image.objects.all()
    # paginator = Paginator(model, per_page=3) # Show 25 contacts per page

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('title', )
    success_url = reverse_lazy('category_list_view')

class ImageListView(ListView):
    model = Image
    paginate_by = 9

class ImageCreateView(CreateView):
    model = Image
    fields = ('picture', 'title', 'description', 'category')
    success_url = reverse_lazy('category_list_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

class ImageUpdateView(UpdateView):
    model = Image
    fields = ('picture', 'title', 'description')
    success_url = reverse_lazy('image_list_view')

class ImageDeleteView(DeleteView):
    model = Image
    success_url = reverse_lazy('image_list_view')

    def get_queryset(self):
        if self.request.user:
            return Image.objects.all()
        return []

class ImageDetailView(DetailView):
    model = Image
    

class CommentCreateView(CreateView):
    model = Comment
    fields = ('comment',)
    def get_success_url(self, **kwargs):
        return reverse_lazy('image_detail_view', args=[int(self.kwargs['pk'])])

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     instance.comment_image = Image.objects.get(id=self.kwargs['pk'])
    #     return super().form_valid(form)


    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.comment_image = Image.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    model = Comment
    fields = ('comment', )
    def get_success_url(self, **kwargs):
        comment_id = Comment.objects.get(id = self.kwargs['pk']).comment_image.id
        return reverse('image_detail_view', args=[comment_id])

class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('category_detail_view')

    def get_queryset(self):
        if self.request.user:
            return Comment.objects.all()
        return []
