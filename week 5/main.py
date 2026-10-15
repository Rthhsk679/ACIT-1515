from menu_data import csv_text

def split(text): #splits string into dictionary
    menu = {}

    for line in text.splitlines():
        meal_type, name, quantity, price = (line.split(",", 3)) #splits string into 4 values
        cost = float(price.replace("$", "")) * 1.8 #1.8x markup
        menu.setdefault(meal_type.capitalize(), []).append((name, quantity, cost)) #.setdefault adds meal_type as a key if it does already exist. Then append the 3 values to the key.
    return menu

def format(menu): #organizes the dictionary keys and values into the output lines
    lines = []

    for meal_type, items in menu.items():
        lines.append(f"* {meal_type} Items *")

        for name, quantity, cost in sorted(items): # sorted() sorts alphabetically
            lines.append(f" ${cost:.2f}\t{name}, {quantity}") #rounds cost to 2 decimal points

        lines.append("")
    return "\n".join(lines) #adds spacing

print(format(split(csv_text)))