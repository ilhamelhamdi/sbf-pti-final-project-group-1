from rest_framework import serializers
from .models import Book, Writer, Publisher

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

# bikin serializer buat Writer sama Publisher juga mo
# Sama kyk di atas?
# iya

# eh btw, l
# ok hbs itu aplg?