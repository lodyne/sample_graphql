import strawberry
import strawberry.django
from .models import Book

@strawberry.django.type(Book)
class BookType:
    id: strawberry.ID
    title: str
    author: str
    isbn: str
    published_date: str
    pages: int
    langauge: str
    cover_image: str    