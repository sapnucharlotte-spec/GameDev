# ==============================
# PLAYER DATA
# ==============================

# Brilyante / Player templates
brilyante_stats = {
    1: {
        "plyr_name": "",
        "name": "Apoy",
        "hp": 30,
        "max_hp": 30,
        "atk": 15,
        "def": 10,
        "skill": "Fireball",
        "skill_damage": 30,
        "skill_count": 2,
        "gold": 0,
        "bag": ["low"]
    },

    2: {
        "plyr_name": "",
        "name": "Tubig",
        "hp": 30,
        "max_hp": 30,
        "atk": 14,
        "def": 12,
        "skill": "Tsunami",
        "skill_damage": 28,
        "skill_count": 2,
        "gold": 0,
        "bag": []
    },

    3: {
        "plyr_name": "",
        "name": "Hangin",
        "hp": 30,
        "max_hp": 30,
        "atk": 13,
        "def": 11,
        "skill": "Tornado",
        "skill_damage": 26,
        "skill_count": 2,
        "gold": 0,
        "bag": []
    },

    4: {
        "plyr_name": "",
        "name": "Lupa",
        "hp": 30,
        "max_hp": 30,
        "atk": 11,
        "def": 15,
        "skill": "Earthquake",
        "skill_damage": 22,
        "skill_count": 2,
        "gold": 0,
        "bag": []
    },
}


# ==============================
# PLAYER FUNCTIONS
# ==============================

def displayPlayerStat(player):
    print(f"\n===== {player['plyr_name']} Statistics =====")
    print(f"Brilyante: {player['name']}")
    print(f"HP: {player['hp']} / {player['max_hp']}  |  ATK: {player['atk']}  |  Defense: {player['def']}")
    print(f"Special Skill: {player['skill']}  |  Skill Damage: {player['skill_damage']}  |  Uses: {player['skill_count']}")
    print(f"Gold: {player['gold']}")


def createPlayer():
    print("\n" + "="*20)

    name = input("What is your name? ").capitalize()

    print("\nChoose your Brilyante:")

    while True:

        try:
            choice = int(input("1. Brilyante ng Apoy\n2. Brilyante ng Tubig\n3. Brilyante ng Hangin\n4. Brilyante ng Lupa\nEnter choice: "))

            if choice in brilyante_stats:
                break

            print("Invalid choice!")

        except ValueError:
            print("Enter numbers only!")

    player = brilyante_stats[choice].copy()

    player["plyr_name"] = name

    print(f"\nWelcome, {name}!")
    print(f"You chose Brilyante ng {player['name']}")

    displayPlayerStat(player)

    return player


def post_level_reward(player):
    print("\n===== LEVEL CLEARED =====")

    player["skill_count"] = 3
    player["hp"] = player["max_hp"]

    print("Skill count restored!")
    print(f"HP restored to {player['max_hp']}!")


