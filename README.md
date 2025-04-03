# Project Description

This is a Django-based project for managing books, authors, and publishers. It provides a web interface using Django views and Tailwind CSS and REST API based on Django Rest Framework for data, along with features like importing books from JSON files.

## Installation

### Prerequisites

- Python 3.10 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- Node.js and npm (for Tailwind CSS)

### Steps

1. Install dependencies:
```bash
poetry install
```

2. Apply database migrations:
```bash
poetry run python manage.py migrate
```

3. Run:
```bash
poetry run python manage.py runserver
```