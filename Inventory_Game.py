import keyboard

inventory = ["Neon Mask", "EMP Bomb", "Cyber Chip", "Energy Drink"]

print("--- WELCOME TO SHIBUYA BLACK MARKET ---")
print("For buy press 'A' | For sale press 'B' | For quit press 'Esc'\n")

print(f"List: {inventory}")

while True:
    pressed_button = keyboard.read_key()

    if pressed_button == "a":

        keyboard.send("backspace")
        try:
            for_buy = int(input("Which item do you want to buy? (Write the number on the list) "))
            print(f"Great, item number {for_buy} selected.")
            for_buy -= 1
            bought_item = inventory.pop(for_buy)
            print(f"You bought {bought_item}!")
            print(f"Remaining inventory: {inventory}")

        except IndexError:
            print("Error: Invalid index, choose another item!")
        except ValueError:
            print("Error: You must enter a number!")

    elif pressed_button == "b":

        keyboard.send("backspace")

        for_sell = input("\nWhich item do you want to sell? Please enter: ")
        inventory.append(for_sell.title())
        print(f"Sale successful! New item added. Current inventory: {inventory}")

    elif pressed_button == "esc":
        print("Exiting system. Wiping tracks...")
        break