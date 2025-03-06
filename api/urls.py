from django.urls import path
from .views import upload_csv, get_challenges

urlpatterns = [
    path('upload-csv/', upload_csv, name='upload_csv'),
    path('challenges/', get_challenges, name='get_challenges'),
]
