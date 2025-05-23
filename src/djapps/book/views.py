from django.http import HttpResponse
from strawberry.django.views import GraphQLView

from .schema import schema
# Create your views here.

graphql_view = GraphQLView.as_view(
    schema=schema,
    graphiql=True,
    # csrf_exempt=True,  # Uncomment if you want to disable CSRF protection
)

def index(request):
    return HttpResponse ("Hello, world. You're at the book index.")


