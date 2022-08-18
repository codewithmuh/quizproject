
from rest_framework import generics
from rest_framework.response import Response
from .models import Quizzes, Questions
from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView
# Create your views here.

# This class is a list view of the Quizzes model, and it returns the data using the QuizSerializer.
class Quiz(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()

# It takes a topic as a parameter, and returns a random question from the database
class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs) :
        questions = Questions.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(questions, many=True)
        return Response(serializer.data)


# The class QuizQuestion inherits from APIView and has a get method that takes in a request, a format,
# and a keyword argument. The get method then filters the Questions model by the quiz_title keyword
# argument and serializes the data
class QuizQuestion(APIView):
     def get(self, request, format=None, **kwargs) :
        quiz = Questions.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)