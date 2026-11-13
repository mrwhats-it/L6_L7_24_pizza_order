TOPPINGS = {"cheese": 40, "olives": 30, "onion": 20, "paneer": 50}
SIZES = {"S": 8, "M": 10, "L": 12}

def toppings_price(toppings_csv):
    # Returns None for non-string input, empty items or unknown toppings
    if not isinstance(toppings_csv, str):
        return None
    total = 0
    for t in toppings_csv.split(','):
        name = t.strip().lower()
        if name not in TOPPINGS:
            return None
        total += TOPPINGS[name]
    return total

def pizza_inches(size):
    # Returns None for non-string input or a size other than S/M/L
    if not isinstance(size, str):
        return None
    return SIZES.get(size.strip().upper())

def split_bill(text):
    # Returns None unless text is "<total>/<people>" with total >= 0 and people >= 1
    if not isinstance(text, str):
        return None
    parts = text.split('/')
    if len(parts) != 2:
        return None
    try:
        total, people = int(parts[0]), int(parts[1])
    except ValueError:
        return None
    if total < 0 or people < 1:
        return None
    try:
        return round(total / people, 2)
    except OverflowError:
        return None

def main():
    print("==== Running toppings_price ====")
    user_input = input("Enter toppings as CSV (e.g. cheese,olives): ")
    result = toppings_price(user_input)
    if result is None:
        print("Invalid toppings. Choose from:", ", ".join(TOPPINGS))
    else:
        print("Toppings Price:", result)

    print("\n==== Running pizza_inches ====")
    user_input = input("Enter pizza size (S/M/L): ")
    result = pizza_inches(user_input)
    if result is None:
        print("Invalid size. Choose from:", "/".join(SIZES))
    else:
        print("Size in Inches:", result)

    print("\n==== Running split_bill ====")
    user_input = input("Enter total and people (e.g. 900/3): ")
    result = split_bill(user_input)
    if result is None:
        print("Invalid input. Use <total>/<people> with total >= 0 and people >= 1")
    else:
        print("Per Person:", result)

if __name__ == "__main__":
    main()
