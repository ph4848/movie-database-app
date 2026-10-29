# Movie Database App 

A simple movie database application built with Python, SQLite, and Streamlit. The application provides a user-friendly interface for managing movie information without writing SQL queries manually.

## Features

- **View Movies:** Display movie records stored in the database.
- **Search by ID:** Retrieve a movie using its unique ID.
- **Insert Movies:** Add new movies with their title, country, release year, and IMDb rating.
- **Update Movies:** Change a movie's release year and IMDb rating.
- **Delete Movies:** Remove a movie from the database.
- **Persistent Storage:** Store movie records in an SQLite database.

## Technologies Used

- **Python** — application logic
- **SQLite** — relational database
- **Streamlit** — interactive web interface

## Project Structure

```text
movie-database-app/
    ├── src/
    │   ├── app_py.py
    │   ├── app_ui.py
    └── requierments.txt
├── MoviesInfo.db        
└── README.md
```
## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ph4848/movie-database-app.git
cd movie-database-app
```

### 2. Create a virtual environment

Create a virtual environment in the project root:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```
## Run the Application

From the project root, run:

```bash
python -m streamlit run src/app_ui.py
```

Streamlit will start a local web server and provide a URL, usually:

```text
http://localhost:8501
```

Open that address in your browser to use the application.

## Database Schema

The application uses a `movies` table with the following columns:

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Auto-incrementing primary key |
| `title` | TEXT | Movie title (required) |
| `country` | TEXT | Country associated with the movie |
| `year` | TEXT | Movie release year |
| `imdb_rate` | REAL | IMDb rating |

The table is created automatically when the database initialization code runs.

## How to Use

1. Start the Streamlit application.
2. Select an operation from the sidebar.
3. Enter the requested movie information or ID.
4. Click the corresponding button to perform the operation.
5. View the results in the application.