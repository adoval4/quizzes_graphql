"""
Project schema
"""

# Grpahene
import graphene

# Schemas
import Users.schema
import Quizzes.schema


class Query(
    Users.schema.Query,
    Quizzes.schema.Query,
    graphene.ObjectType
    ):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(
    Quizzes.schema.Mutation, 
    graphene.ObjectType
    ):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)