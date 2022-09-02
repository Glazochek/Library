import graphene
from graphene_django import DjangoObjectType
from todoapp.models import TODO, Project


class TODOType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TODOMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        text = graphene.String(required=True)

    todo = graphene.Field(TODOType)

    @classmethod
    def mutate(cls, root, info, text, id):
        todo = TODO.objects.get(id=id)
        todo.text = text
        todo.save()
        return TODOMutation(todo=todo)


class Mutation(graphene.ObjectType):
    update_todo = TODOMutation.Field()


class Query(graphene.ObjectType):

    all_todo = graphene.List(TODOType)
    all_project = graphene.List(ProjectType)
    todo_id = graphene.Field(TODOType, id=graphene.Int(required=True))
    project_name = graphene.List(ProjectType, name=graphene.String(required=False))

    def resolve_all_todo(root, info):
        return TODO.objects.all()

    def resolve_all_project(root, info):
        return Project.objects.all()

    def resolve_todo_id(self, info, id):
        try:
            return TODO.objects.get(id=id)
        except TODO.DoesNotExist:
            return None

    def resolve_project_name(self, info, name=None):
        project = Project.objects.all()
        if name:
            project = project.filter(name=name)
        return project


schema = graphene.Schema(query=Query,  mutation=Mutation)
