import strawberry
from strawberry.types import Info
from .models import Book
from .types import BookType

@strawberry.type
class Query:
    @strawberry.field
    def books(self, info: Info) -> list[BookType]:
        """
        Get all books.
        """
        return Book.objects.all()
    
schema = strawberry.Schema(query=Query)
    
    