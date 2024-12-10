from django.urls import path
from blogging.views import BlogListView, BlogDetailView, SignupView

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("posts/<int:post_id>/", BlogDetailView.as_view(), name="blog_detail"),
]
