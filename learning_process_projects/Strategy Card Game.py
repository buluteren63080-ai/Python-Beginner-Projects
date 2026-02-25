hero_profile = ("Shadow Mage", 150)

card_catalog = {
    "A1": {"name": "Fireball", "damage": 20},
    "A2": {"name": "Quick Strike", "damage": 10},
    "S1": {"name": "Ice Shield", "damage": 0},
    "E1": {"name": "Poison Dagger", "damage": 15}
}

turn_moves = ["A1", "A2", "A1", "S1"]

print(f"--- {hero_profile[0]} Turn Summary ---")

'''
#card_id turn_moves listesindeki stringleri alıp sırayla card_catalog dict içine yazdırıyor
# A1 A2 gibi stringler card_catalog için key görevi görüyor ama sözlük içinde sçzlük olduğu için 
iki tane kalın parantez ile damage key nin altındaki değer alınıyor sum ile toplanıyor.
'''
total_damage = sum([card_catalog[card_id]["damage"] for card_id in turn_moves])

#set de tekrar eden olmadığı için unique_cards kümesine tekrar edenler silinip alınıyor.
unique_cards = set(turn_moves)

print(f"Base Damage: {total_damage}")

if len(unique_cards) >= 3:
    total_damage += 15
    print("COMBO ACTIVATED! 3 different cards played. (+15 Bonus Damage)")
else:
    print("Not enough variety for a combo.")

print(f"Total Damage Dealt to Enemy: {total_damage}")