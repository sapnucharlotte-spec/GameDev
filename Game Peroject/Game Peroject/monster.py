from random import randint, choice
# ==============================
# ENEMY DATA
# ==============================

dungeons = {
    "Agavar": {
        "Ascendant": "Agane", "Info": "Deep beneath Hathoria lies a cursed combat ground. Survive the roaming bandidos and reach its depths—where the silent executioner, Agane, awaits.",
        "Enemies": {
            1: {"name": "Bandido", "hp": 25, "atk": randint(7,12), "def": 8, "gold": 10, "info": "ruthless group of rouge fights"},
            2: {"name": "Agane", "hp": 40, "atk": randint(13,18), "def": 10, "gold": 170, "info": "silent executioner, right hand commander of Hathoria’s army", 
                "loot": "Goblet of Vital Essence", "l-info": "A mystical silver goblet infused with ancient life energy. Grants +10 Health to its wielder."}
        }
    },
    "Hagwarth": {
        "Ascendant": "Hagorn", "Info": "A massive underground throne fortress lies beneath Hathoria, guarded by loyal Hathorians who kill all intruders without mercy. Survive their unyielding defense, and face the will of King Hagorn—a ruthless ruler.",
        "Enemies": {
            1: {"name": "Hathorian", "hp": 30, "atk": randint(12,17), "def": 10, "gold": 30, "info": "loyal elite soldiers"},
            2: {"name": "Hagorn", "hp": 75, "atk": randint(30,50), "def": 25, "gold": 350, "info": "cunning and power-hungry ruler", 
                "loot": "Twinblade Arc Wand", "l-info": "A rare dual-purpose weapon combining two enchanted blades with arcane magic. Grants +15 Attack."}
        }
    },
    "Etheris": {
        "Ascendant": "Ether", "Info": "A sacred underground chamber sealed by ancient magic, where pashnea-born fragments of a cursed Bathaluman linger in the dark. Only those who survive their wrath may enter the final depth—where Ether, the cursed goddess, lies imprisoned.",
        "Enemies": {
            1: {"name": "Ethrak", "hp": 40, "atk": randint(18,23), "def": 19, "gold": 50, "info": "corrupted pashnea’s born from fragments of Ether’s cursed divine power"},
            2: {"name": "Ether", "hp": 100, "atk": randint(55,75), "def": 30, "gold": 680, "info": "A cursed Bathaluman goddess bound in serpent form", 
                "loot": "Aegis Etherplate", "l-info": "A legendary armor forged from condensed ether crystals, known for its unmatched resilience. Grants +20 Defense."}
        }
    }
}