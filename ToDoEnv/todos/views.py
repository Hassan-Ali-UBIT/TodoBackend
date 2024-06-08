from django.shortcuts import render
from .serializer import TodoSerializer
from .models import Todos
from rest_framework import generics, mixins
from .mixins import TodoEditorPermissionMixin
# Create your views here.


class get_view(generics.ListAPIView, TodoEditorPermissionMixin):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'

class update_view(generics.RetrieveUpdateDestroyAPIView, TodoEditorPermissionMixin):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'

class retrieve_view(generics.RetrieveAPIView, TodoEditorPermissionMixin):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'

show_view = get_view.as_view()
updelete_view = update_view.as_view()
get_specific_view = retrieve_view.as_view()

class TodoView(generics.GenericAPIView, 
               mixins.CreateModelMixin,
               mixins.DestroyModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin, 
               TodoEditorPermissionMixin):
    
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
generalview = TodoView.as_view()