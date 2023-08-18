const addBookForm = document.getElementById('add-book-form');
const bookList = document.getElementById('book-list');

// Function to display books on the page
function displayBooks(books) {
    bookList.innerHTML = '';
    books.forEach(book => {
        const li = document.createElement('li');
        li.innerHTML = `<span>Title:</span> ${book.title}<br><span>Author:</span> ${book.author}<br><button class="delete-btn" data-id="${book.id}">Delete</button>`;
        bookList.appendChild(li);
    });

    // Attach event listeners to delete buttons
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', async (event) => {
            const bookId = event.target.getAttribute('data-id');
            await fetch(`/books/${bookId}`, { method: 'DELETE' });
            loadBooks();
        });
    });
}

// Function to load and display books
async function loadBooks() {
    const response = await fetch('/books');
    const books = await response.json();
    displayBooks(books);
}

// Add book form submission
addBookForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    await fetch('/books', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, author })
    });
    addBookForm.reset();
    loadBooks();
});

// Load books on page load
loadBooks();
