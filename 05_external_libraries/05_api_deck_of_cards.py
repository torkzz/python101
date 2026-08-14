"""
Working with REST APIs: Deck of Cards API

Concepts:
- Sending GET requests to external REST APIs.
- Extracting dynamic route parameters (`deck_id`).
- Parsing nested JSON arrays and objects.
- Inspecting HTTP metadata (Status code, Headers, Remaining cards count).
"""

import requests


def run_card_dealer_game() -> None:
    base_url = "https://deckofcardsapi.com/api/deck"

    # 1. Create a new shuffled deck
    response = requests.get(f"{base_url}/new/shuffle/?deck_count=1", timeout=5)
    print("=== 1. New Deck Response Metadata ===")
    print("HTTP Status Code:", response.status_code)
    print("Server Header   :", response.headers.get("Server"))

    deck_data = response.json()
    print("Deck Data Object:", deck_data)

    deck_id = deck_data["deck_id"]
    print("Shuffled Deck ID:", deck_id)
    print("Total Cards     :", deck_data["remaining"])

    # 2. Draw 2 cards for the player
    player_resp = requests.get(f"{base_url}/{deck_id}/draw/?count=2", timeout=5)
    player_data = player_resp.json()

    # 3. Draw 2 cards for the dealer
    dealer_resp = requests.get(f"{base_url}/{deck_id}/draw/?count=2", timeout=5)
    dealer_data = dealer_resp.json()

    # 4. Draw 5 community cards
    community_resp = requests.get(f"{base_url}/{deck_id}/draw/?count=5", timeout=5)
    community_data = community_resp.json()

    print("\n=== 2. Game Cards Draw Results ===")

    print("PLAYER CARDS:")
    for card in player_data["cards"]:
        print(f"  - {card['value']} OF {card['suit']} (Image: {card['image']})")

    print("\nDEALER CARDS:")
    for card in dealer_data["cards"]:
        print(f"  - {card['value']} OF {card['suit']} (Code: {card['code']})")

    print("\nCOMMUNITY CARDS:")
    for card in community_data["cards"]:
        print(f"  - {card['value']} OF {card['suit']}")

    # 5. Check remaining cards count in deck
    final_deck_check = requests.get(f"{base_url}/{deck_id}/", timeout=5).json()
    print("\n=== 3. Deck Summary ===")
    print("Remaining Cards in Deck:", final_deck_check.get("remaining"))


if __name__ == "__main__":
    try:
        run_card_dealer_game()
    except requests.RequestException as err:
        print("API Error:", err)
