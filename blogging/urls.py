from django.urls import path
from blogging.views import BlogListView, PostDetailView, SignupView

urlpatterns = [
    path("post/<int:post_id>/", PostDetailView.as_view(), name="blog_detail"),
    path("", BlogListView.as_view(), name="blog_index"),
    path("signup/", SignupView.as_view(), name="signup"),
]
