
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Todos
import json

class TodoSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='todo-list', lookup_field="pk")
    edit_url = serializers.SerializerMethodField(read_only=True)
    owner = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Todos
        fields = ['owner','url','edit_url', 'pk', 'task','content' ,'completion']

    def get_edit_url(self, obj):
        request = self.context.get("request")

        if request is None:
            return None
        
        return reverse("todo-detail", kwargs={"pk": obj.pk}, request=request)
    
    def get_owner(self, obj):
        data = {}

        data['user'] = obj.user.username
        data['id'] = obj.user.id

        return data