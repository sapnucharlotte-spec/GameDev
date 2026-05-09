from attack_system import deal_damage
from character import (
    createPlayer,
    displayPlayerStat,
    post_level_reward
)
from monster import dungeons
from item_gold import shop, checkBag


# ==============================
# MENUS
# ==============================

main_menu = (
    "1. Proceed to shop",
    "2. Check Bag",
    "3. Continue to next dungeon"
    "4. Exit"
)

battle_menu = (
    "1. Basic Attack",
    "2. Special Skill",
    "3. Exit Battle"
)


# ==============================
# UTILITY
# ==============================

def display_menu(menu):

    for item in menu:
        print(item)


# ==============================
# BATTLE SYSTEM
# ==============================

def player_turn(player, enemy):
    print(f"\n===== {player['plyr_name'].upper()} TURN =====")

    print(f"Your HP: {player['hp']} / {player['max_hp']}")
    print(f"{enemy['name']} HP: {enemy['hp']}")

    display_menu(battle_menu)

    move = input("Choose attack: ")

    # BASIC ATTACK
    if move == "1":

        damage = deal_damage(
            player["atk"],
            enemy["def"],
            enemy
        )

        print(f"\nYou dealt {damage} damage!")
        print(f"{enemy['name']} HP is now {enemy['hp']}")

    # SKILL ATTACK
    elif move == "2":

        if player["skill_count"] <= 0:
            print("\nNo skills remaining!")
            return True

        damage = deal_damage(
            player["skill_damage"],
            enemy["def"],
            enemy
        )

        player["skill_count"] -= 1

        print(f"\nYou used {player['skill']}!")
        print(f"You dealt {damage} damage!")
        print(f"Skill uses left: {player['skill_count']}")

    # EXIT
    elif move == "3":
        print("\nYou exited the battle!")
        return False

    else:
        print("Invalid move!")

    return True


def enemy_turn(player, enemy):
    print(f"\n===== {enemy['name'].upper()} TURN =====")

    damage = deal_damage(
        enemy["atk"],
        player["def"],
        player
    )

    print(f"{enemy['name']} attacked!")
    print(f"{enemy['name']} dealt {damage} damage!")

    print(f"Your HP is now {player['hp']} / {player['max_hp']}")


def startGame(player):
    for dungeon_name in dungeons:
        dungeon_info = dungeons[dungeon_name]["Info"]

        print(f"\n===== DUNGEON: {dungeon_name.upper()} =====")

        print(f"Info: {dungeon_info}")

        for enemy_id in dungeons[dungeon_name]['Enemies']:

            enemy_data = dungeons[dungeon_name]['Enemies'][enemy_id]

            repeat_count = 3 if enemy_id == 1 else 1


            for fight in range(1, repeat_count + 1):

                enemy = enemy_data.copy()
                
                print(f"\nA wild {enemy['name']} {fight} appeared!")
                print(f"Info: {enemy['info']}")

                # if enemy_id == 1:
                #     print("\n[Tutorial Enemy]")
                #     print("Choose attacks using numbers.")

                while player["hp"] > 0 and enemy["hp"] > 0:

                    continue_battle = player_turn(player, enemy)

                    if continue_battle is False:
                        return

                    if enemy["hp"] <= 0:

                        print(f"\n{enemy['name']} was defeated!")

                        player["gold"] += enemy["gold"]

                        print(f"You earned {enemy['gold']} Gold!")

                        player["skill_damage"] += 3

                        print("Your special skill became stronger!")
                        print(f"Skill Damage increased by 5!")
                        print(f"Current Skill Damage: {player['skill_damage']}")

                        post_level_reward(player)

                        displayPlayerStat(player)

                        if enemy_id == 2:
                            print("\n" + "="*20)
                            print(f"CONGRATULATIONS! {enemy['name']} dropped {enemy['loot']}, check bag to use.")
                            print(f"Description: {enemy['l-info']}")
                            print("You defeated all enemies!")

                            player['bag'].append(enemy['loot'])

                            while True:
                                display_menu(main_menu)

                                try:
                                    choice = int(input("Choose Action: "))

                                    if choice == 1:
                                        shop(player, displayPlayerStat)
                                        break

                                    elif choice == 2:
                                        checkBag(player)

                                    elif choice == 3:
                                        break

                                    elif choice == 4:
                                        print("Thanks for playing!")
                                        return

                                    else:
                                        print("Invalid choice!")

                                except ValueError:
                                    print("Invalid input!")
                        break

                    enemy_turn(player, enemy)

                    if player["hp"] <= 0:

                        print(f"\nYou were defeated by {enemy['name']}!")

                        player["hp"] = player["max_hp"]
                        player["skill_count"] = 3

                        # if enemy_id == 1:

                        #     print("\nRetrying tutorial battle...")

                        #     enemy = enemy_stats[enemy_id].copy()

                        # else:

                        player["gold"] += 20

                        print("You received 20 Gold.")
                        print(f"Current Gold: {player['gold']}")

                        # print("\nYou were brought back to the shop.")

                        # shop(player, displayPlayerStat)

                        enemy = enemy_data.copy()

                        print(f"\nYou are challenging {enemy['name']} again!")
            


        # ==============================
        # INTRO
        # ==============================

def intro():
    print("Welcome to Encantadia!")

    start = input("Ready for adventure? [YES or NO]: ").upper()

    if start == "YES":

        player = createPlayer()

        print("\n===== TUTORIAL =====")
        print("Defeat enemies to earn gold.")
        print("Use skills wisely.")
        print("After every dungeon, you may visit the shop.\n")

        startGame(player)

    else:
        print("You left the game!")


# ==============================
# START GAME
# ==============================

if __name__ == "__main__":
    intro()