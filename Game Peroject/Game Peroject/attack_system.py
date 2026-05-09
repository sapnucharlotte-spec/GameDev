# ==============================
# ATTACK SYSTEM
# ==============================


def attack_system(attacker_atk, defender_def, defender_hp):
    damage = attacker_atk - defender_def
    
    if damage < 1:
        damage = 1

    defender_hp -= damage

    return defender_hp, damage


def deal_damage(attacker_power, defender_def, target):
    target["hp"], damage = attack_system(
        attacker_power,
        defender_def,
        target["hp"]
    )

    target["hp"] = max(0, target["hp"])

    return damage