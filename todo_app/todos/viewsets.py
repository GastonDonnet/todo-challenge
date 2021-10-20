from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_fields = {
        'created_at': ['gte', 'lte', 'exact'],
        'name': ['icontains'],
        'description': ['icontains'],
    }