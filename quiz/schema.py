from unicodedata import category
from .models import *
import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField

class CategoryType(DjangoObjectType):
    class Meta:
        model=Category

class QuizzesType(DjangoObjectType):
    class Meta:
        model=Quizzes

class QuestionType(DjangoObjectType):
    class Meta:
        model=Question 

class AnswerType(DjangoObjectType):
    class Meta:
        model=Answer


class Query(graphene.ObjectType):
    all_quizzes = DjangoListField(QuizzesType)
    quizzes= graphene.Field(QuizzesType,id=graphene.Int())

    question= graphene.Field(QuestionType,id=graphene.ID())
    all_question_answers=graphene.List(AnswerType,id=graphene.ID())

    def resolve_all_quizzes(root,info):
        return Quizzes.objects.all()

    def resolve_quizzes(root,info,id):
        return Quizzes.objects.get(pk=id)

    def resolve_question(root,info,id):
        return Question.objects.get(pk=id)
    
    def resolve_all_question_answers(root,info,id):
        return Answer.objects.filter(question=id)

class CategoryMutation(graphene.Mutation):
    
    class Arguments:
        id=graphene.ID()
        name=graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls,root,info,name,id=None):
        if id==None:
            category=Category(name=name)
            
        else:
            category=Category.objects.get(id=id)
            category.name=name
            
        category.save()
        return CategoryMutation(category=category)
            
class CategoryDeleteMutation(graphene.Mutation):
    class Arguments:
        id=graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls,root,info,id=None):
        category=Category.objects.get(id=id)
        category.delete()
        return 

class Mutation(graphene.ObjectType):
    update_category =CategoryMutation.Field()
    delete_category= CategoryDeleteMutation.Field()

schema=graphene.Schema(query=Query,mutation=Mutation)