"""
Asynchronous Programming & Concurrent Execution (asyncio)

Concepts:
- Async functions (`async def`) and `await` keywords.
- Event loop execution (`asyncio.run()`).
- Offloading blocking synchronous functions (e.g., `requests.get`) to background threads using `asyncio.to_thread()`.
- Concurrent execution of multiple tasks using `asyncio.gather()`.
- Unpacking generator expressions (`*(...)`) into `asyncio.gather()`.
"""

import asyncio
import requests


def load_webpage(url: str) -> str:
    """Blocking synchronous HTTP request for a given URL."""
    return requests.get(url, timeout=5).text


async def demo_single_async() -> None:
    print("=== 1. Single Task with asyncio.to_thread ===")
    result = await asyncio.to_thread(load_webpage, "https://example.com")
    print(f"Fetched HTML ({len(result)} bytes):")
    print(result[:100].strip())


async def demo_concurrent_gather() -> None:
    print("\n=== 2. Concurrent Execution with asyncio.gather ===")
    urls = [
        "https://example.com",
        "https://example.org",
        "https://example.net"
    ]

    # Run multiple blocking load_webpage calls concurrently in separate threads
    results = await asyncio.gather(
        *(asyncio.to_thread(load_webpage, url) for url in urls)
    )

    print(f"Fetched {len(results)} URLs concurrently:")
    for idx, result in enumerate(results, start=1):
        print(f"Result {idx} ({len(result)} bytes): {result[:60].strip()}...")


async def main() -> None:
    await demo_single_async()
    await demo_concurrent_gather()


if __name__ == "__main__":
    asyncio.run(main())
    print("\nConcurrent asyncio tasks completed.")
