from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from blogging.models import Post, Category
from django.http import Http404
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


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
        queryset = Post.objects.prefetch_related("categories").all()
        if self.request.user.is_authenticated:
            return queryset
        else:
            return queryset[:2]


class BlogDetailView(DetailView):

    model = Post
    template_name = "blogging/detail.html"
    pk_url_kwarg = "posts"


class SignupView(CreateView):
    model = get_user_model()
    form_class = UserCreationForm
    template_name = "blogging/signup.html"

    def get_success_url(self):
        return redirect("login")
