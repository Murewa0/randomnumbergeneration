import random


def middle_square_method(seed, num_digits=4):
    """Generate a sequence of middle square numbers with specified number of digits."""
    current_value = seed
    while True:
        squared_value = current_value**2
        squared_str = str(squared_value).zfill(
            num_digits * 2
        )  # Ensure the squared value has enough digits
        middle_digits = int(
            squared_str[
                len(squared_str) // 2
                - num_digits // 2 : len(squared_str) // 2
                + num_digits // 2
            ]
        )
        current_value = middle_digits
        yield middle_digits


def generate_recharge_card():
    """Generate a recharge card consisting of four 4-digit tuples."""
    # Generate four different seeds for each card
    seeds = [random.randint(1000, 9999) for _ in range(4)]
    generators = [middle_square_method(seed) for seed in seeds]
    card = "-".join([str(next(gen)).zfill(4) for gen in generators])
    return card


def generate_multiple_recharge_cards(num_cards):
    """Generate a specified number of recharge cards."""
    cards = [generate_recharge_card() for _ in range(num_cards)]
    return cards


# Ask the user for the number of recharge cards
num_cards = int(input("Enter the number of recharge cards to generate: "))

# Generate and print the recharge cards
recharge_cards = generate_multiple_recharge_cards(num_cards)
for idx, card in enumerate(recharge_cards):
    print(f"Recharge Card {idx + 1}: {card}")
