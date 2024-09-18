from biblioteca_app.models import Shelf

def count_books_on_shelf(shelf_id): # Libros por estante
    shelf = Shelf.objects.get(id=shelf_id)
    return shelf.books.count()

def calculate_shelf_fill_percentage(shelf_id): # Porcentaje de lleno
    shelf = Shelf.objects.get(id=shelf_id)
    return (shelf.books.count() / shelf.max_capacity) * 100

def calculate_total_shelf_value(shelf_id): # Precio total de libro
    shelf = Shelf.objects.get(id=shelf_id)
    return sum(book.price for book in shelf.books.all())

def get_most_expensive_book(shelf_id): # Más caro
    shelf = Shelf.objects.get(id=shelf_id)
    return shelf.books.order_by('-price').first()

def get_books_ordered_by_name(shelf_id): # Ordenamiento
    shelf = Shelf.objects.get(id=shelf_id)
    return shelf.books.order_by('name')
