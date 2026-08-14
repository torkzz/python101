"""
HTTP Requests with the `requests` Library

Concepts:
- Making GET requests (`requests.get`).
- Inspecting status codes (`status_code`), headers (`headers`), and HTML content (`text`).
- Sending POST requests with JSON payloads (`json=...`) and custom headers (`headers=...`).
- Parsing JSON responses (`response.json()`).
"""

import requests


def demo_http_get() -> None:
    print("=== 1. Basic HTTP GET Request ===")
    response = requests.get("https://httpbin.org/get", timeout=5)

    print("Status Code:", response.status_code)
    print("JSON Response keys:", list(response.json().keys()))

    print("\n=== 2. Fetching Webpage Content ===")
    pagedata = requests.get("https://example.com", timeout=5)
    print("Content-Type Header:", pagedata.headers.get("Content-Type"))
    print("HTML Length:", len(pagedata.text))


def demo_http_post() -> None:
    print("\n=== 3. HTTP POST Request with JSON Payload & Headers ===")
    
    json_payload = {
        "name": "Allen",
        "age": 25,
        "city": "Pasig"
    }

    request_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Content-Type": "application/json"
    }

    # Making POST request to httpbin.org/post (reliable echo endpoint)
    response = requests.post(
        "https://httpbin.org/post",
        headers=request_headers,
        json=json_payload,
        timeout=5
    )

    rq_json = response.json()
    parsed_json = rq_json.get("json", {})

    print("Status Code:", response.status_code)
    print(
        "Name: {}, Age: {}, City: {}".format(
            parsed_json.get("name"),
            parsed_json.get("age"),
            parsed_json.get("city")
        )
    )


if __name__ == "__main__":
    try:
        demo_http_get()
        demo_http_post()
    except requests.RequestException as e:
        print("Network request failed:", e)
