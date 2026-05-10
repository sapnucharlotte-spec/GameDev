from character import brilyante_stats, displayPlayerStat

# ==============================
# SHOP ITEMS
# ==============================

# Shop items
shop_items = {
    1: {
        "name": "Health Kit",
        "stat": "max_hp",
        "add": 8,
        "price": 45,
        "info": "Increase HP"
    },

    2: {
        "name": "Attack Kit",
        "stat": "atk",
        "add": 3,
        "price": 60,
        "info": "Increase Attack"
    },

    3: {
        "name": "Skill Upgrade",
        "stat": "skill_damage",
        "add": 4,
        "price": 75,
        "info": "Increase Skill Damage"
    },

    4: {
        "name": "Defense Upgrade",
        "stat": "def",
        "add": 2,
        "price": 60,
        "info": "Increase Defense"
    },
}


# ==============================
# SHOP MENU
# ==============================

shop_menu = (
    "1. Buy",
    "2. Continue to next dungeon"
)


# ==============================
# SHOP FUNCTIONS
# ==============================

def upgrade_stat(player, stat, amount):
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

# ==============================
# ITEM FUNCTIONS
# ==============================


def checkBag(player):
    print("\nYour Backpack:")
    while True:
        for i, item in enumerate(player['bag'], 1):
            print(f"{i}. {item}")
        try:
            choice_num = int(input("\nEnter item number to use [0 to cancel]: "))
            if 1 <= choice_num <= len(player['bag']):
                item = player['bag'].pop(choice_num - 1)
                print(f"You used {item}!")
                artiReward(player,item)
                
            elif choice_num == 0:
                print("Canceled.")
                return
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid input. Enter a number.")



def artiReward(player, artifact):
    if artifact == "Goblet of Vital Essence":
        player['max_hp'] += 5
        player['hp'] = player['max_hp']
        print("\n===== UPDATED STATS =====")
        displayPlayerStat(player)
    elif artifact == "Twinblade Arc Wand":
        player['atk'] += 4
    elif artifact == "Aegis Etherplate":
        player['def'] += 5
    return player