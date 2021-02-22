import graphene
from graphene_django import DjangoObjectType

from . import models


class BookType(DjangoObjectType):
    class Meta:
        model = models.Books
        fields = ("id", "title", "desc")


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)


schema = graphene.Schema(query=Query)