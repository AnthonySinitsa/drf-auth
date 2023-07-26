from rest_framework import generics
from .serializer import NotCloudSerializer
from .models import NotCloud
from .permissions import IsOwnerOrReadOnly

class NotCloudList(generics.ListCreateAPIView):
  queryset = NotCloud.objects.all()
  serializer_class = NotCloudSerializer
  
class NotCloudDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = NotCloud.objects.all()
  serializer_class = NotCloudSerializer