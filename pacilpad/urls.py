from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ListBook, ListPublisher, ListWriter, UnitBook, UnitPublisher, UnitWriter

urlpatterns = [
    path('book/', ListBook.as_view()),
    path('book/<int:id>', UnitBook.as_view()),
    path('writer/', ListWriter.as_view()),
    path('writer/<int:id>', UnitWriter.as_view()),
    path('publisher/', ListPublisher.as_view()),
    path('publisher/<int:id>', UnitPublisher.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)