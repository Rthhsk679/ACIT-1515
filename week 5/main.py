from menu_data import csv_text

def get_name(item):
    return item[0]

def split(text):
    menu = {}

    for line in text.strip().splitlines():
        meal_type, name, quantity, price = (line.split(",", 3))
        cost = float(price.replace("$", "")) * 1.8
        menu.setdefault(meal_type.lower(), []).append((name, quantity, cost))
    return menu

def format(menu):
    lines = []

    for meal_type, items in menu.items():
        lines.append(f"* {meal_type} Items *")

        for name, quantity, cost in sorted(items, key = get_name):
            lines.append(f" ${cost:.2f}\t{name}, {quantity}")

        lines.append("")
    return "\n".join(lines)

print(format(split(csv_text)))