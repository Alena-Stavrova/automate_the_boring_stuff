#Chapter 7

#Write a function named display_inventory() that would take any possible “inventory” and display it like the following:
#Inventory:
#12 arrow
#42 gold coin
#1 rope
#6 torch
#1 dagger
#Total number of items: 62

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

#display_inventory(stuff)

#Imagine that the same fantasy video game represents a vanquished dragon’s loot as a list of strings, like this:
#dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#Write a function named add_to_inventory(inventory, added_items).
#The inventory parameter is a dictionary representing the player’s inventory (as in the previous project) and the added_items parameter is a list, like dragon_loot.
#The add_to_inventory() function should return a dictionary that represents the player’s updated inventory. Note that the added_items list can contain multiples of the same item.
#Your code could look something like this:

def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory[i] = 1
    return(inventory)

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
