from django.urls import path
from .views import NotCloudsList, NotCloudsDetail

urlpatterns = [
  path('', NotCloudsList.as_view(), name='not_clouds_list'),
  path('<int:pk>/', NotCloudsDetail.as_view(), name='not_clouds_detail'),
]