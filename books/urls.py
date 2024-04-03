from django.urls import path

from .views import BookListView, BookDetailView, SearchResultsListView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'), # new, 1
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'), # new 2, for making book links to have its own ID
    path('search', SearchResultsListView.as_view(), name='search_results'), # new 3

]