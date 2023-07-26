from rest_framework import generics
from .serializer import NotCloudSerializer
from .models import NotCloud
from .permissions import IsOwnerOrReadOnly

class NotCloudsList(generics.ListCreateAPIView):
  queryset = NotCloud.objects.all()
  serializer_class = NotCloudSerializer
  
class NotCloudsDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = NotCloud.objects.all()
  serializer_class = NotCloudSerializer