from django.urls import path
from blogging.views import BlogListView, BlogDetailView
from blogging import views

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("signup/", views.signup, name="signup"),
    path("posts/<int:post_id>/", BlogDetailView.as_view(), name="blog_detail"),
]
