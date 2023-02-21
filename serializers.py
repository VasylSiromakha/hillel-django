from rest_framework import serializers

from books.models import Book, Country, Author


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name")


class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.IntegerField(read_only=True)
    average_price = serializers.FloatField(read_only=True)

    class Meta:
        model = Author
        fields = ("first_name", "last_name", "books_count", "average_price")


class BookSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ("id", "name", "country", "authors", "seller", "price", "is_archived")