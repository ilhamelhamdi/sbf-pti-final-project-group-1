from django.shortcuts import render
from django.http import Http404
from pacilpad.models import Book, Writer, Publisher
from .serializers import BookSerializer, WriterSerializer, PublisherSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Handle /book
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

    def post(self, request):
        try:
            newBook = BookSerializer(data=request.data)
            if newBook.is_valid():
                newBook.save()
                context = {
                    'status': 201,
                    'message': 'success'
                }
                return Response(context, status=status.HTTP_201_CREATED)
        except:
            context = {
                'status': 500,
                'message': 'failed'
            }
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Handle /book/<int:id>
class UnitBook(APIView):
    def get_book(self, id):
        try:
            book = Book.objects.get(pk=id)
            return book
        # Check wheter book is available or not
        except:
            raise Http404

    def get(self, request, id):
        try:
            book = self.get_book(id)
            context = {
                'status': 200,
                'message': 'success',
                'data': BookSerializer(book).data
            }
            return Response(context, status=status.HTTP_200_OK)
        # Book Not Found
        except Http404:
            context = {
                "status": 404,
                "message": 'failed'
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)
        # Server Error
        except:
            context = {
                'status': 500,
                'message': 'failed'
            }
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            old_book = self.get_book(id)
            updated_book = BookSerializer(old_book, data=request.data)
            if updated_book.is_valid():
                updated_book.save()
                context = {
                    "status": 202,
                    "message": 'success',
                }
                return Response(context, status=status.HTTP_202_ACCEPTED)
            else:
                # request.data input from user is not valid
                context = {
                    "status": 400,
                    "message": 'failed',
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            context = {
                "status": 404,
                "message": 'failed'
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)
        except:
            context = {
                'status': 500,
                'message': 'failed'
            }
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        try:
            book = self.get_book(id)
            book.delete()
            context = {
                "status": 200,
                "message": 'success',
            }
            return Response(context, status=status.HTTP_200_OK)
        except Http404:
            context = {
                "status": 404,
                "message": 'failed'
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)
        except:
            context = {
                'status': 500,
                'message': 'failed'
            }
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Handle /book
class ListWriter(APIView):
    def get(self, request):
        try:
            allWriter = Writer.objects.all()
            context = {
                'status': 200,
                'message': 'success',
                'data': WriterSerializer(allWriter, many=True).data
            }
            return Response(context, status=status.HTTP_200_OK)
        except :
            context = {
                'status': 500,
                'message': 'failed'
            }
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            newWriter = WriterSerializer(data=request.data)
            if newWriter.is_valid():
                newWriter.save()
                context = {
                    'status': 201,
                    'message': 'success'
                }
                return Response(context, status=status.HTTP_201_CREATED)
        except:
            context = {
                'status': 500,
                'message': 'failed'
            }
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Handle /writer/<int:id>
class UnitWriter(APIView):
    def get_writer(self, id):
        try:
            writer = Writer.objects.get(pk=id)
            return writer
        except Exception as e:
            raise Http404
    
    def get(self, request, id):
        try:
            writer = self.get_writer(id)
            context = {
                'status': 200,
                'message': 'success',
                'data': WriterSerializer(writer).data
            }
            return Response(context, status=status.HTTP_200_OK)
        except Http404:
            context = {
                "status": 404,
                "message": 'failed'
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)
        except:
            context = {
                'status': 500,
                'message': 'failed'
            }
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            old_writer = self.get_writer(id)
            updated_writer = WriterSerializer(old_writer, data=request.data)
            if updated_writer.is_valid():
                updated_writer.save()
                context = {
                    "status": 202,
                    "message": 'success',
                }
                return Response(context, status=status.HTTP_202_ACCEPTED)
            else:
                context = {
                    "status": 400,
                    "message": 'failed',
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            context = {
                "status": 404,
                "message": 'failed'
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)
        except:
            context = {
                'status': 500,
                'message': 'failed'
            }
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        try:
            writer = self.get_writer(id)
            writer.delete()
            context = {
                "status": 200,
                "message": 'success',
            }
            return Response(context, status=status.HTTP_200_OK)
        except Http404:
            context = {
                "status": 404,
                "message": 'failed'
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)
        except:
            context = {
                'status': 500,
                'message': 'failed'
            }
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Handle /publisher
class ListPublisher(APIView):
    def get(self, request):
        try:
            allPublisher = Publisher.objects.all()
            context = {
                'status': 200,
                'message': 'success',
                'data': PublisherSerializer(allPublisher, many=True).data
            }
            return Response(context, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            context = {
                'status': 500,
                'message': 'failed'
            }
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            newPublisher = PublisherSerializer(data=request.data)
            if newPublisher.is_valid():
                newPublisher.save()
                context = {
                    'status': 201,
                    'message': 'success'
                }
                return Response(context, status=status.HTTP_201_CREATED)
        except:
            context = {
                'status': 500,
                'message': 'failed'
            }
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Handle /publisher/<int:id>
class UnitPublisher(APIView):
    def get_publisher(self, id):
        try:
            publisher = Publisher.objects.get(pk=id)
            return publisher
        except:
            raise Http404
    
    def get(self, request, id):
        try:
            publisher = self.get_publisher(id)
            context = {
                'status': 200,
                'message': 'success',
                'data': PublisherSerializer(publisher).data
            }
            return Response(context, status=status.HTTP_200_OK)
        except Http404:
            context = {
                "status": 404,
                "message": 'failed'
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)
        except:
            context = {
                'status': 500,
                'message': 'failed'
            }
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            old_publisher = self.get_writer(id)
            updated_publisher = PublisherSerializer(old_publisher, data=request.data)
            if updated_publisher.is_valid():
                updated_publisher.save()
                context = {
                    "status": 202,
                    "message": 'success',
                }
                return Response(context, status=status.HTTP_202_ACCEPTED)
            else:
                context = {
                    "status": 400,
                    "message": 'failed',
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            context = {
                "status": 404,
                "message": 'failed'
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)
        except:
            context = {
                'status': 500,
                'message': 'failed'
            }
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        try:
            publisher = self.get_publisher(id)
            publisher.delete()
            context = {
                "status": 200,
                "message": 'success',
            }
            return Response(context, status=status.HTTP_200_OK)
        except Http404:
            context = {
                "status": 404,
                "message": 'failed'
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)
        except:
            context = {
                'status': 500,
                'message': 'failed'
            }
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)