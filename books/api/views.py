from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def book(request):
    books = ['Fluent Python', 'Eloquent Javascript',
             'Pro python', 'Speaking Javascript', 'Go to the Programing Language']
    return Response(status=status.HTTP_200_OK, data={'data': books})
