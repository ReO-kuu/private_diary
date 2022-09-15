# from django.conf import settings
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    #トップページ
    path('',views.IndexView.as_view(),name="index2"),
    path('inquiry/',views.InquiryView.as_view(),name="inquiry2"),
]