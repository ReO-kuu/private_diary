from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    #トップページ
    path('',views.IndexView.as_view(),name="index"),
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
    path('diary-list/',views.DiaryListView.as_view(),name="diary_list"),
    path('diary-detail/<int:pk>',views.DiaryDetailView.as_view(),name="diary_detail"),
    path('diary-create/',views.DiaryCreateView.as_view(), name="diary_create"),
    path('diary-updata/<int:pk>/',views.DiaryUpdateView.as_view(), name="diary_update"),
    path('diary-delete/<int:pk>/',views.DiaryDeleteView.as_view(), name="diary_delete"),
]