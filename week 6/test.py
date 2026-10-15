csv_text = """lunch,bento box b - sashimi,box combo,$9.59
dinner,vegetable sushi,6 rolls,$3.50
dinner,tuna roll,3 rolls,$4.50
dinner,roe,2 rolls,$3.95
lunch,bento box a - chicken teriyaki,box combo,$8.59
dessert,cheesecake,1 slice,$8.00"""

def split(text): #splits string into dictionary
    menu = {}

    for line in text.splitlines():
        meal_type, name, quantity, price = (line.split(",", 3)) #splits string into 4 values
        menu.setdefault(meal_type.capitalize(), []).append((name, quantity, price))
    return menu

print(split(csv_text))