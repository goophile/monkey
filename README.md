Monkey
======

A simple Flask app to demonstrate the usage of GraphQL and mongoengine.

Python GraphQL libraries:

| Library                       | Package Name   | Base                   | Description                          |
| ----------------------------- | -------------- | ---------------------- | ------------------------------------ |
| graphql-python/graphql-core   | graphql        |                        | Python port of GraphQL.js            |
| graphql-python/graphql-server | graphql_server | graphql-core           | Helper for building GraphQL servers  |
| graphql-python/flask-graphql  | flask_graphql  | graphql-server         | GraphQL support for Flask            |
| graphql-python/graphene       | graphene       | graphql-core           | GraphQL with code-first approach     |
| graphql-python/graphene-mongo | graphene_mongo | graphene + mongoengine | Mongoengine integration for Graphene |

Start with

```sh
$ docker-compose up -d --build
$ docker logs monkey_monkey_1 -f
```

Example query:

```sh
$ curl -X POST -d '{ user (email: "william@monkey.com") { email firstName } }' 10.17.2.2/graphql
$ curl -X POST -d '{ users  { email firstName } }' 10.17.2.2/graphql
$ curl -X POST -d '{ posts  { title content } }' 10.17.2.2/graphql
```

Example mutation:

```sh
$ curl -X POST -d 'mutation mUser { createUser (email: "aa@b.com", firstName: "aa", lastName: "test") { user {email firstName} ok } }' 10.17.2.2/graphql
$ curl -X POST -d 'mutation dUser { deleteUser (email: "aa@b.com") { user {email firstName} ok } }' 10.17.2.2/graphql
```
