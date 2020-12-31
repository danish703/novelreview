from django.urls import path
from .views import details,genreNovelList
urlpatterns = [
    path('<int:id>', details,name='details'),
    path('genre/<int:cid>',genreNovelList,name='genreNovelList'),
]