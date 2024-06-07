from rest_framework.routers import DefaultRouter
from todos.viewsets import todoViewSet

router = DefaultRouter()

router.register('todos-abc', todoViewSet, basename='todos')

urlpatterns = router.urls