from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from blogging.models import Post
from django.http import Http404
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class BlogTemplateView(TemplateView):

    template_name = "stub.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["args"] = self.args
        context["kwargs"] = self.kwargs
        return context


class BlogListView(ListView):
    model = Post
    published = model.objects.exclude(published_date__exact=None)
    queryset = published.order_by("-published_date")
    template_name = "blogging/list.html"
    context_object_name = "posts"


class BlogDetailView(DetailView):

    model = Post
    published = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"
    pk_url_kwarg = "post_id"

    def get_object(self):
        post_id = self.kwargs.get("post_id")
        return get_object_or_404(self.published, pk=post_id)


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})
