# ==============================
# SHOP ITEMS
# ==============================

# Shop items
shop_items = {
    1: {
        "name": "Health Kit",
        "stat": "max_hp",
        "add": 10,
        "price": 55,
        "info": "Increase HP"
    },

    2: {
        "name": "Attack Kit",
        "stat": "atk",
        "add": 25,
        "price": 80,
        "info": "Increase Attack"
    },

    3: {
        "name": "Skill Upgrade",
        "stat": "skill_damage",
        "add": 35,
        "price": 100,
        "info": "Increase Skill Damage"
    },

    4: {
        "name": "Defense Upgrade",
        "stat": "def",
        "add": 25,
        "price": 80,
        "info": "Increase Defense"
    },
}


# ==============================
# SHOP MENU
# ==============================

shop_menu = (
    "1. Buy",
    "2. Continue to next level"
)


# ==============================
# SHOP FUNCTIONS
# ==============================

def upgrade_stat(player, stat, amount):
    """Upgrade player stats."""

    if stat == "max_hp":

        player["max_hp"] += amount

        player["hp"] = min(
            player["max_hp"],
            player["hp"] + amount
        )

    else:
        player[stat] += amount

    print(f"{stat.upper()} increased by {amount}!")


def buy_item(player, item_choice):
    """Buy shop item."""

    if item_choice not in shop_items:
        print("Invalid Item!")
        return

    item = shop_items[item_choice]

    if player["gold"] < item["price"]:
        print("\nNot enough gold!")
        return

    player["gold"] -= item["price"]

    upgrade_stat(
        player,
        item["stat"],
        item["add"]
    )

    print(f"\nYou bought {item['name']}!")
    print(f"Remaining Gold: {player['gold']}")


def display_menu(menu):
    """Display menu options."""

    for item in menu:
        print(item)


def shop(player, displayPlayerStat):

    while True:

        print("\n===== IMAW'S SHOP =====")
        print(f"Gold: {player['gold']}")

        for key, value in shop_items.items():

            print(f"""
[{key}] {value['name']}
Effect : +{value['add']}
Price  : {value['price']} Gold
Info   : {value['info']}
            """)

        display_menu(shop_menu)

        try:
            option = int(input("Choose Action: "))

        except ValueError:
            print("Invalid input!")
            continue

        if option == 1:

            try:
                item_choice = int(input("Enter item number: "))
                buy_item(player, item_choice)

                print("\n===== UPDATED STATS =====")
                displayPlayerStat(player)

            except ValueError:
                print("Invalid item!")

        elif option == 2:
            print("\nProceeding to next level...")
            return

        else:
            print("Invalid Option!")