from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.shortcuts import get_object_or_404

from catalog import models

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': Genre.objects.count()
    }

    return render(request, 'index.html', context=context)


# Create a list view from class
class BookListView(generic.ListView):
    model = Book
    # Define pagination
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginated_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author
# def book_detail_view(request, primary_key):
#     # try:
#     #     book = Book.objects.get(pk=primary_key)
#     # except Book.DoesNotExist:
#     #     raise Http404('Book does not exist')
    
#     # Alternative of code above
#     book = get_object_or_404(Book, pk=primary_key)

#     return render(request, 'catalog/book_detail.html', context={'book': book})