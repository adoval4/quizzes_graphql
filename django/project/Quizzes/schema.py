"""
Quizzes schema
"""

# Graphene
import graphene
from graphene_django.types import DjangoObjectType
from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField

# Models
from Quizzes.models import *


class QuizNode(DjangoObjectType):
	class Meta:
		model = Quiz


class TopicNode(DjangoObjectType):
	class Meta:
		model = Topic


class CreateTopicMutation(graphene.Mutation):
	class Arguments:
		name = graphene.String(required=True)

	topic = graphene.Field(TopicNode)

	def mutate(self, info, name):
		topic = Topic.objects.create(name=name)
		return CreateTopicMutation(topic=topic)


class UpdateTopicMutation(graphene.Mutation):
	class Arguments:
		name = graphene.String(required=True)
		id = graphene.ID()

	topic = graphene.Field(TopicNode)

	def mutate(self, info, name, id):
		topic = Topic.objects.get(pk=id)
		topic.name = name
		topic.save()
		return UpdateTopicMutation(topic=topic)


class Query(graphene.ObjectType):
	topic = graphene.Field(TopicNode, id=graphene.Int())
	all_topics = graphene.List(TopicNode)

	quiz = graphene.Field(QuizNode, id=graphene.Int())
	all_quizzes = graphene.List(QuizNode)

	def resolve_topic(self, info, **kwargs):
		id = kwargs.get('id')
		name = kwargs.get('name')
		if id is not None:
			return Topic.objects.get(pk=id)
		if name is not None:
			return Topic.objects.get(name=name)
		return None

	def resolve_all_topics(self, info, **kwargs):
		return Topic.objects.all()

	def resolve_quiz(self, info, **kwargs):
		id = kwargs.get('id')
		name = kwargs.get('name')
		if id is not None:
			return Quiz.objects.get(pk=id)
		if name is not None:
			return Quiz.objects.get(name=name)
		return None

	def resolve_all_quizzes(self, info, **kwargs):
		return Quiz.objects.all()

class Mutation(graphene.ObjectType):
	update_topic = UpdateTopicMutation.Field()
	create_topic = CreateTopicMutation.Field()
