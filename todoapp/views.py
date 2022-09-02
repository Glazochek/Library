from django.shortcuts import render, get_object_or_404
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import TODO, Project
from .serializers import ProjectSerializers, TODOSerializers
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny


def main(request):
    context = {}
    return render(request, 'todoapp/index.html', context)


class ALimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class BLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
    pagination_class = ALimitOffsetPagination

    @action(detail=True, methods=['get'])
    def article_name_only(self, request, pk=None):
        article = get_object_or_404(Project, pk=pk)
        return Response({'-': article.name})

    def list(self, request):
        articles = Project.objects.all()
        serializer = ProjectSerializers(articles, many=True)
        return Response(serializer.data)


class TODOViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = TODO.objects.all()
    serializer_class = TODOSerializers
    pagination_class = BLimitOffsetPagination
    permissions_classes = [AllowAny]

    @action(detail=True, methods=['get'])
    def article_name_only(self, request, pk=None):
        article = get_object_or_404(TODO, pk=pk)
        return Response({'-': article.text})

    def list(self, request):
        articles = TODO.objects.all()
        serializer = TODOSerializers(articles, many=True)
        return Response(serializer.data)

