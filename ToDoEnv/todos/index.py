from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Todos

@register(Todos)
class TodoIndexer(AlgoliaIndex):
    fields = [
        "task",
        "content",
        "completion"
    ]

    settings = {
        "searchableAttributes": ['task', 'content'],
        "attributesForFaceting": ['completion']
    }
    tags = "get_tag"



