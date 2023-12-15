from django.urls import path
from . import views
urlpatterns = [
    path("",views.homePage,name="home-page"),
    path("post/",views.post,name="all-posts"),
    path("post/<slug:slug>",views.detailPost,name="detail-page")
]