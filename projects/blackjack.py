"""
CLI Blackjack Game with API Integration (Deck of Cards API)

Concepts:
- Fetching external data via REST API (`requests.get`).
- Functions & Modular Design (`create_deck`, `draw_card`, `card_value`, `calculate_value`).
- Game Loop (`while True`, `input()`, conditional branching).
- Dealer Turn & Hidden Cards.
"""

import requests


def create_deck():
    """Create and shuffle 2 decks via API."""
    response = requests.get(
        "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=2"
    )
    return response.json()["deck_id"]


def draw_card(deck_id):
    """Draw 1 card from the specified deck ID."""
    response = requests.get(
        f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1"
    )
    return response.json()["cards"][0]


def card_value(card):
    """Calculate point value for a given card object."""
    value = card["value"]

    if value in ["JACK", "QUEEN", "KING"]:
        return 10
    if value == "ACE":
        return 11
    return int(value)


def calculate_value(cards):
    """Calculate total hand value, adjusting ACE from 11 to 1 on bust."""
    value = sum(card_value(card) for card in cards)
    aces = sum(1 for card in cards if card["value"] == "ACE")

    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value


def play_blackjack():
    print("=== CLI Blackjack ===")
    deck_id = create_deck()

    # Draw initial cards for Player and Dealer
    cards = [draw_card(deck_id), draw_card(deck_id)]
    dealer_cards = [draw_card(deck_id), draw_card(deck_id)]

    # Display initial Dealer hand (1 face up, 1 hidden)
    print("\nDealer Cards:")
    print(f"- {dealer_cards[0]['value']} of {dealer_cards[0]['suit']}")
    print("- [Hidden Card]")

    while True:
        value = calculate_value(cards)

        print("\nPlayer Cards:")
        for card in cards:
            print(f"- {card['value']} of {card['suit']}")
        print(f"Total: {value}")

        if value == 21:
            print("\nBLACKJACK! You win!")
            break

        if value > 21:
            print("\nBUST! You lose!")
            break

        choice = input("\nStand or Hit? [s/h]: ").lower().strip()

        if choice == "s":
            # Dealer turn: reveal cards and hit until >= 17
            print("\nDealer Cards:")
            for card in dealer_cards:
                print(f"- {card['value']} of {card['suit']}")
            dealer_value = calculate_value(dealer_cards)
            print(f"Dealer Total: {dealer_value}")

            while dealer_value < 17:
                new_card = draw_card(deck_id)
                dealer_cards.append(new_card)
                dealer_value = calculate_value(dealer_cards)
                print(f"Dealer draws: {new_card['value']} of {new_card['suit']}")
                print(f"Dealer Total: {dealer_value}")

            # Determine round outcome
            if dealer_value > 21 or value > dealer_value:
                print("\nYou win!")
            elif value < dealer_value:
                print("\nDealer wins!")
            else:
                print("\nTie!")

            again = input("\nPlay again? [y/n]: ").lower().strip()
            if again == "y":
                play_blackjack()
            break

        if choice == "h":
            cards.append(draw_card(deck_id))
            continue

        print("Please enter 's' or 'h'.")


if __name__ == "__main__":
    play_blackjack()
