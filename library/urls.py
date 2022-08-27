from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet
from todoapp.views import main, TODOViewSet, ProjectViewSet

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('todo', TODOViewSet)
router.register('Project', ProjectViewSet)

urlpatterns = [
    path('', main),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('auth/', include('authapp.urls', namespace='auth')),
]