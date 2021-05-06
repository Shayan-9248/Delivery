from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('bucket-list/', views.BucketList.as_view(), name='list'),
    path('download-bucket/<str:key>/', views.DownloadBucket.as_view(), name='download'),
    path('delete-bucket/<str:key>/', views.DeleteBucket.as_view(), name='delete'),
]