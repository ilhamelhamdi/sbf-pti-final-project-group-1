from django.shortcuts import render
from pacilpad.models import Book, Writer, Publisher
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# def data(request):
#     data = Peserta.objects.all()
#     context = {
#         'data': data
#     }
#     return render(request, 'index.html', context)


class ListBook(APIView):
    def get(self, request):
        try:
            allBook = Book.objects.all()
            context = {
                'status': 200,
                'message': 'success',
                'data': BookSerializer(allBook, many=True).data
            }
            return Response(context, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            context = {
                'status': 500,
                'message': 'failed'
            }
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)