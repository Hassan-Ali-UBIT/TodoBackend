from django.shortcuts import render
from .serializer import TodoSerializer
from .models import Todos
from rest_framework import generics, mixins
from rest_framework.response import Response
from .mixins import TodoEditorPermissionMixin
# Create your views here.


class get_view(generics.ListAPIView, TodoEditorPermissionMixin):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        user = request.user

        if not user.is_authenticated:
            return Todos.objects.none()
        
        return qs.filter(user=user)
    
class create_view(generics.CreateAPIView, TodoEditorPermissionMixin):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

post_view = create_view.as_view()


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

from . import client

class search_view(generics.GenericAPIView):
    def get(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Todos.objects.none()
        query = []
        tags = []

        query = request.GET.get('q') 
        tags = request.GET.get('tag')
        completion = str(request.GET.get('completion')) != "0"
        if not query:
            return Response("", status=400)
        
        result = client.perform_search(query, tags=tags, completion=completion)

        

        return Response(result)