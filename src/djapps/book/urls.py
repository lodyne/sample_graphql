from django.urls import path
from .views import graphql_view, index
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("graphql/",csrf_exempt(graphql_view) , name="graphql"),
    path("", index, name="index")
]
