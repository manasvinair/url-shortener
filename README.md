---

# URL Shortener

A simple Streamlit web app that shortens long URLs using the TinyURL service.

## Features

- Accepts a long URL as input.
- Generates a short version using the TinyURL API via the `pyshorteners` library.
- Allows users to copy the shortened URL directly to their clipboard.

## Requirements

Install the necessary Python packages:

```bash
pip install streamlit pyshorteners pyperclip
```

## How to Run

Start the app by running:

```bash
streamlit run url_shortner.py
```

## Usage

1. Open the app in your browser.
2. Enter a URL into the input field.
3. Click the **"SHORTEN"** button.
4. The shortened URL will be displayed.
5. Click **"COPY"** to copy it to your clipboard.

---
