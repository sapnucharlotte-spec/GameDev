from random import randint, choice
# ==============================
# ENEMY DATA
# ==============================

dungeons = {
    "Agavar": {
        "Ascendant": "Agane", "Info": "Deep beneath Hathoria lies a cursed combat ground. Survive the roaming bandidos and reach its depths—where the silent executioner, Agane, awaits.",
        "Enemies": {
            1: {"name": "Bandido", "hp": 18, "atk": randint(3,6), "def": 2, "gold": 15, "info": "ruthless group of rouge fights"},
            2: {"name": "Agane", "hp": 32, "atk": randint(7,10), "def": 4, "gold": 120, "info": "silent executioner, right hand commander of Hathoria’s army", 
                "loot": "Goblet of Vital Essence", "l-info": "A mystical silver goblet infused with ancient life energy. Grants +5 Health to its wielder."}
        }
    },
    "Hagwarth": {
        "Ascendant": "Hagorn", "Info": "A massive underground throne fortress lies beneath Hathoria, guarded by loyal Hathorians who kill all intruders without mercy. Survive their unyielding defense, and face the will of King Hagorn—a ruthless ruler.",
        "Enemies": {
            1: {"name": "Hathorian", "hp": 40, "atk": randint(9,13), "def": 5, "gold": 35, "info": "loyal elite soldiers"},
            2: {"name": "Hagorn", "hp": 80, "atk": randint(16,22), "def": 8, "gold": 250, "info": "cunning and power-hungry ruler", 
                "loot": "Twinblade Arc Wand", "l-info": "A rare dual-purpose weapon combining two enchanted blades with arcane magic. Grants +4 Attack."}
        }
    },
    "Etheris": {
        "Ascendant": "Ether", "Info": "A sacred underground chamber sealed by ancient magic, where pashnea-born fragments of a cursed Bathaluman linger in the dark. Only those who survive their wrath may enter the final depth—where Ether, the cursed goddess, lies imprisoned.",
        "Enemies": {
            1: {"name": "Ethrak", "hp": 55, "atk": randint(14,18), "def": 10, "gold": 55, "info": "corrupted pashnea’s born from fragments of Ether’s cursed divine power"},
            2: {"name": "Ether", "hp": 120, "atk": randint(22,30), "def": 16, "gold": 500, "info": "A cursed Bathaluman goddess bound in serpent form", 
                "loot": "Aegis Etherplate", "l-info": "A legendary armor forged from condensed ether crystals, known for its unmatched resilience. Grants +5 Defense."}
        }
    }
}