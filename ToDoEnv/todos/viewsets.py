from rest_framework import viewsets

from .models import Todos
from .serializer import TodoSerializer

class todoViewSet(viewsets.ModelViewSet):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "pk"