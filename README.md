# URL Shortener

A lightweight Python application that creates short aliases for URLs and keeps track of their usage.

## Overview

URL Shortener is a console application that simulates a local URL shortening service. It generates unique short codes, records visits, and displays usage statistics.

The project demonstrates object-oriented programming, modular design, and basic data processing.

## Features

- Create short URLs
- Resolve aliases
- Track visit count
- Display statistics
- View visit history

## Project Structure

```
.
├── main.py
├── link.py
├── registry.py
├── generator.py
├── analytics.py
├── history.py
├── sample_urls.py
├── settings.py
└── README.md
```

## Example Output

```
========= URL SHORTENER =========

Python Docs
Short URL: pQ3xA7
Visits: 2

GitHub
Short URL: Lk9Pm2
Visits: 1

--------------------------
Stored Links: 3
Total Visits: 5
```

## Technologies

- Python 3
- Git
- GitHub

## Future Improvements

- SQLite storage
- QR code generation
- Expiring links
- Password protection
- REST API

