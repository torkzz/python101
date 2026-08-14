import requests

def calculate_values(val: str) -> int:
  if val.lower() in ["jack", "queen", "king"]:
    return 10
  elif val.lower() == "ace":
    return 1
  else:
    return int(val)

def card_formatter(card: dict) -> str:
  return "{} of {}".format(card["value"].capitalize(), card["suit"].capitalize())

def draw_cards(deck_seed: str, count: int = 1) -> list:
  return requests.get("https://deckofcardsapi.com/api/deck/{}/draw/".format(deck_seed), params={"count": count}, headers=_REQUEST_HEADERS).json()["cards"]

_REQUEST_HEADERS = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Trailer/93.3.8652.5",
  "Content-Type": "application/json"
}

deck_seed = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/", params={"deck_count": 2}, headers=_REQUEST_HEADERS).json()["deck_id"]

current_card_value = 0

initial_draw = draw_cards(deck_seed, 2)

print("Your initial cards:")
for i in initial_draw:
  current_card_value += calculate_values(i["value"])
  print(card_formatter(i))

print("Total value:", current_card_value)

while True:
  response = input("Stand? (type 'y' to stand and quit) ")
  if response.lower() == "y":
    break
  else:
    print()
    new_draw = draw_cards(deck_seed, 2)[0]
    current_card_value += calculate_values(new_draw["value"])
    print(card_formatter(new_draw))
    print("Total value:", current_card_value)

    if current_card_value == 21:
      print("BLACKJACK!!!")
      break
    elif current_card_value > 21:
      print("BUST!!!!!")
      break;
    else:
      continue
