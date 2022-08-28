from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todoapp.views import main, TODOViewSet, ProjectViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('todo', TODOViewSet)
router.register('project', ProjectViewSet)

urlpatterns = [
    path('', main, name='main'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('api-token-auth/', views.obtain_auth_token)
]
