document.addEventListener('DOMContentLoaded', function() {
    const filterForm = document.getElementById('filterForm');

    if (filterForm) {
        filterForm.addEventListener('submit', function(e) {
            e.preventDefault(); // Previene el envío por defecto del formulario

            const shelf = document.getElementById('shelf').value;
            const genre = document.getElementById('genre').value;

            // Mostrar indicador de carga
            const booksDisplay = document.getElementById('booksDisplay');
            booksDisplay.innerHTML = '<p>Cargando...</p>';

            // Hacer una solicitud fetch para obtener los libros filtrados
            fetch(`/filter-books/?shelf=${shelf}&genre=${genre}`)
                .then(response => response.json())
                .then(data => {
                    booksDisplay.innerHTML = ''; // Limpiar los libros anteriores

                    // Mostrar los libros filtrados
                    if (data.books && data.books.length > 0) {
                        data.books.forEach(book => {
                            const bookItem = document.createElement('div');
                            bookItem.innerHTML = `<h3>${book.title}</h3>
                                                  <p>Autor: ${book.author}</p>
                                                  <p>Género: ${book.genre}</p>
                                                  <p>Precio: $${book.price}</p>`;
                            booksDisplay.appendChild(bookItem);
                        });
                    } else {
                        booksDisplay.innerHTML = '<p>No hay libros disponibles para esta selección.</p>';
                    }
                })
                .catch(error => {
                    booksDisplay.innerHTML = '<p>Ocurrió un error al obtener los libros.</p>';
                });
        });
    } else {
        console.error("No se encontró el formulario de filtro.");
    }
});
