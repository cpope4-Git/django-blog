from django.urls import path, include

from blogging.models import Category
from blogging.views import (
    BlogListView,
    BlogDetailView,
    SignupView,
    UserViewSet,
    CategoryViewSet,
    PostViewSet,
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"posts", PostViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = [
    path(
        "posts/<int:post_id>/",
        BlogDetailView.as_view(pk_url_kwarg="post_id"),
        name="blog_detail",
    ),
    path("blogging/", BlogListView.as_view(), name="blog_index"),
    path("", BlogListView.as_view(), name="blog_index"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
