from rest_framework import serializers
from todoapp.models import Project, TODO


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TODOSerializers(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'

