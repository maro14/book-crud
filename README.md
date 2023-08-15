
# Flask Book CRUD App with Docker and MongoDB

## Overview

This documentation provides an overview of a Flask CRUD (Create, Read, Update, Delete) application integrated with Docker for containerization and MongoDB for data storage. The application allows users to manage a collection of books using a RESTful API.

## Table of Contents

- [Flask Book CRUD App with Docker and MongoDB](#flask-book-crud-app-with-docker-and-mongodb)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Project Structure](#project-structure)
  - [Setup and Installation](#setup-and-installation)
  - [Running the Application](#running-the-application)
  - [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Contributing](#contributing)
  - [License](#license)

## Prerequisites

- Docker: Install Docker to create and manage containers for your application.
- Docker Compose: Install Docker Compose to define and run multi-container Docker applications.

## Project Structure

The project is organized with the following structure:

```
my-book-app/
│
├── app/
│   ├── static/
│   │   ├── styles.css
│   │   └── scripts.js
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   └── run.py
│
├── Pipfile
├── Pipfile.lock
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore
```

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd my-book-app
   ```

2. Install Docker and Docker Compose if not already installed.

3. Build and start the containers:
   ```bash
   docker-compose up
   ```

## Running the Application

Access the Flask app in your web browser at `http://localhost:5000`. Use the provided API endpoints to interact with the app programmatically.

## Usage

- Add a new book: Fill in the "Title" and "Author" fields on the web interface and click "Add Book."
- List books: View the list of books on the web interface or use the `/books` API endpoint.
- View, update, or delete a book: Click on a book in the list to view details, update, or delete it.

## API Endpoints

- `GET /books`: Get a list of all books.
- `POST /books`: Add a new book.
- `GET /books/<book_id>`: View details of a specific book.
- `PUT /books/<book_id>`: Update details of a specific book.
- `DELETE /books/<book_id>`: Delete a specific book.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
