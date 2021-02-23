import graphene
from graphene_django import DjangoObjectType, DjangoListField

from . import models


class DivisionType(DjangoObjectType):
    class Meta:
        model = models.Division
        fields = "__all__"


class DistrictType(DjangoObjectType):
    class Meta:
        model = models.District
        fields = "__all__"


class Query(graphene.ObjectType):
    divisions = graphene.Field(DivisionType, id=graphene.Int())
    districts = graphene.List(DistrictType, id=graphene.Int())

    def resolve_divisions(root, info, id):
        return models.Division.objects.get(id=id)

    def resolve_districts(root, info, id):
        return models.District.objects.filter(division=id)


class DivisionMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    division = graphene.Field(DivisionType)

    @classmethod
    def mutate(cls, root, info, *args, **kwargs):
        id = kwargs.pop("id")
        obj = models.Division.objects.get(id=id)
        obj.__dict__.update(kwargs)
        obj.save()
        return DivisionMutation(division=obj)


class Mutation(graphene.ObjectType):
    add_division = DivisionMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)