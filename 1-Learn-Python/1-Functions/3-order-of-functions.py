def main():
    health = 10
    armour = 5
    add_armour(health, armour)

def add_armour(health,armour):
    new_health = health+armour
    print_health(new_health)

def print_health(new_health):
    print(f"The player has now {new_health} health")

# call endpoint at last
main()