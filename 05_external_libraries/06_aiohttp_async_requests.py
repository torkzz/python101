"""
Native Asynchronous HTTP Requests with aiohttp

Concepts:
- Native async HTTP client (`aiohttp.ClientSession()`).
- Double async context manager (`async with ClientSession()` & `async with session.get()`).
- Asynchronous response reading (`await r.text()`).
- Sync vs Async comparison: Non-blocking thread yields control back to event loop while waiting for network I/O.
"""

import asyncio
import aiohttp


# 1. Single Async Webpage Request
async def load_single_webpage() -> None:
    print("=== 1. Single Webpage Load with aiohttp ===")
    # ClientSession handles HTTP connection pooling
    async with aiohttp.ClientSession() as session:
        # session.get opens non-blocking HTTP GET request stream
        async with session.get("https://example.com") as r:
            # await r.text() asynchronously reads body without blocking event loop
            v = await r.text()
            print(f"Response Status: {r.status}")
            print("First 100 chars of HTML:")
            print(v[:100].strip())


# 2. Concurrent Async Webpage Requests with asyncio.gather()
async def fetch_url(session: aiohttp.ClientSession, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()


async def load_multiple_webpages_concurrently() -> None:
    print("\n=== 2. Concurrent Webpage Loads with aiohttp + asyncio.gather ===")
    urls = [
        "https://example.com",
        "https://example.org",
        "https://example.net",
    ]

    async with aiohttp.ClientSession() as session:
        # Launch 3 async HTTP requests concurrently on event loop
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

        for url, html in zip(urls, results):
            print(f"Fetched {url} -> {len(html)} bytes")


if __name__ == "__main__":
    # Start asyncio event loop
    asyncio.run(load_single_webpage())
    print("\nLoading webpage with a non-blocking operation (asyncio) finished.")

    # Concurrent demonstration
    asyncio.run(load_multiple_webpages_concurrently())
