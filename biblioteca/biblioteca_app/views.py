from django.http import JsonResponse
from .models import Book 
from django.shortcuts import render
from .services.shelf_services import (
    count_books_on_shelf, 
    calculate_shelf_fill_percentage,
    calculate_total_shelf_value, 
    get_most_expensive_book,
    get_books_ordered_by_name,  )

def shelf_detail(request, shelf_id):
    context = {
        'book_count': count_books_on_shelf(shelf_id),
        'fill_percentage': calculate_shelf_fill_percentage(shelf_id),
        'total_value': calculate_total_shelf_value(shelf_id),
        'most_expensive_book': get_most_expensive_book(shelf_id),
        'books_ordered': get_books_ordered_by_name(shelf_id),
    }
    return render(request, 'biblioteca_app/shelf_detail.html', context)

def filter_books(request):
    shelf_id = request.GET.get('shelf')
    genre = request.GET.get('genre')

    # No hay validación de parámetros
    books = Book.objects.filter(shelf_id=shelf_id, genre__icontains=genre)

    books_data = [
        {
            'title': book.name,
            'author': book.author,
            'genre': book.genre,
            'price': book.price,
        }
        for book in books
    ]

    return JsonResponse({'books': books_data})


def home(request):
    return render(request, 'biblioteca_app/home.html')