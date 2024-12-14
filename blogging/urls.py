from django.urls import path
from blogging.views import BlogListView, BlogDetailView, SignupView

urlpatterns = [
    path(
        "posts/<int:post_id>/",
        BlogDetailView.as_view(pk_url_kwarg="post_id"),
        name="blog_detail",
    ),
    path("blogging/", BlogListView.as_view(), name="blog_index"),
    path("", BlogListView.as_view(), name="blog_index"),
    path("signup/", SignupView.as_view(), name="signup"),
]
