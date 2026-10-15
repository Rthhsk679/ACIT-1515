from menu_data import csv_text

def parse_menu(text):
    menu = []
    for line in text.strip().splitlines():
        meal_type, name, quantity, price = line.split(",", 3)
        cost = float(price.strip().replace("$", "")) * 1.8
        menu.append((meal_type, name, quantity, cost))
    return menu

def format_menu(menu):
    meal_types = []
    for meal_type, name, quantity, cost in menu:
        if meal_type not in meal_types:
            meal_types.append(meal_type)

    lines = []
    for meal_type in meal_types:
        lines.append(f"* {meal_type.title()} Items *")

        items = []
        for item_type, name, quantity, cost in menu:
            if item_type is meal_type:
                items.append((name, quantity, cost))

        for name, quantity, cost in sorted(items):
            lines.append(f" ${cost:.2f}\t{name}, {quantity}")
        lines.append("")
    return "\n".join(lines)

print(format_menu(parse_menu(csv_text)))