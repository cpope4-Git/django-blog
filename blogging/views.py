from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from blogging.models import Post, Category
from django.http import Http404
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from blogging.serializers import PostSerializer, UserSerializer, CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BlogTemplateView(TemplateView):

    template_name = "blogging/stub.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["args"] = self.args
        context["kwargs"] = self.kwargs
        return context


class BlogListView(ListView):
    model = Post
    template_name = "blogging/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        published = Post.objects.exclude(published_date__exact=None)
        return published


class BlogDetailView(DetailView):

    model = Post
    template_name = "blogging/detail.html"
    context_object_name = "post"

    def get_queryset(self):
        published = Post.objects.exclude(published_date__exact=None)
        return published


class SignupView(CreateView):
    model = get_user_model()
    form_class = UserCreationForm
    template_name = "blogging/signup.html"

    def get_success_url(self):
        return redirect("login")
