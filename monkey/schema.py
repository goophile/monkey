"""
GraphQL schema.
"""
import logging
from graphene import ObjectType, Field, List, String, Boolean, Schema, Mutation

from . import model


class User(ObjectType):
    email = String()
    first_name = String()
    last_name = String()

    def resolve_first_name(parent, info):
        logging.info('parent mongo ID: %s', parent.id)
        return parent.first_name


class CreateUser(Mutation):
    class Arguments:
        email = String()
        first_name = String()
        last_name = String()

    ok = Boolean()
    user = Field(lambda: User)

    def mutate(root, info, email, first_name, last_name):
        new_user = model.User(email=email, first_name=first_name, last_name=last_name).save()
        ok = True
        return CreateUser(ok=ok, user=new_user)


class DeleteUser(Mutation):
    class Arguments:
        email = String()

    ok = Boolean()
    user = Field(lambda: User)

    def mutate(root, info, email):
        to_del = model.User.objects(email=email)[0]
        to_del.delete()
        ok = True
        return DeleteUser(ok=ok, user=to_del)


class Post(ObjectType):
    title = String()
    content = String()


class Query(ObjectType):
    goodbye = String()
    user = Field(User, email=String())
    users = List(User)
    posts = List(Post)

    def resolve_goodbye(root, info):
        return 'See ya!'

    def resolve_user(root, info, email):
        return list(model.User.objects(email=email))[0]

    def resolve_users(root, info):
        return model.User.objects()

    def resolve_posts(root, info):
        return model.Post.objects()


class Mutation(ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()


schema = Schema(query=Query, mutation=Mutation)
