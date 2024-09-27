
# URL Shortener API

A simple URL shortener API built with Flask that allows users to shorten URLs and retrieve the original URLs from the shortened versions.

## Features

- Generate short URLs for any provided URL.
- Redirect from a short URL to the original URL.
- Duplicate URLs return the same shortened URL.
- JSON-based storage of URLs.

## Project Structure

```
url_shortener/
│
├── app.py                  # Main application entry point
├── config.py               # Configuration settings
├── routes.py               # API routes for URL shortening and redirection
├── core/                   # Business logic for URL shortening and managing the DB
│   ├── compute.py          # Logic for generating short URLs
│   └── crud.py             # Logic for managing JSON (DB in future)
└── mapped_urls.json        # JSON file to store URLs
└── test.py                 # Unit test for API route
└── README.md               # Project documentation
└── requirements.txt        # List of dependencies
```

## Requirements

Make sure you have Python 3.7 or above installed. Install the necessary dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Run the Application

To start the Flask development server, run:

```bash
python app.py
```

By default, the app runs at `http://127.0.0.1:5000/`.

### 2. API Endpoints

#### Shorten a URL (POST `/api/shorten`)

This endpoint accepts a long URL and returns a shortened version.

- **Method**: POST
- **URL**: `/api/shorten`
- **Body (JSON)**:
  ```json
  {
    "url": "https://jysk.fi/kylpyhuone/kylpyhuonetarvikkeet/suihkutarvikkeet/suihkuverhorenkaat-vara-12-kpl/pkt"
  }
  ```
- **Response (JSON)**:
  ```json
  {
    "short_url": "-ZD1zLDi"
  }
  ```

**Example using curl**:
```bash
curl -X POST http://127.0.0.1:5000/api/shorten -H "Content-Type: application/json" -d '{"url": "https://jysk.fi/kylpyhuone/kylpyhuonetarvikkeet/suihkutarvikkeet/suihkuverhorenkaat-vara-12-kpl/pkt"}'
```

#### Redirect to Original URL (GET `/<short_url>`)

This endpoint redirects the user to the original URL based on the short URL.

- **Method**: GET
- **URL**: `/<short_url>`

Example:
```
http://127.0.0.1:5000/-ZD1zLDi
```
