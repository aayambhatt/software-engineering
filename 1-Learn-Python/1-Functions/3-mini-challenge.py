"""
🔧 Challenge: Simulate a Simple Game Flow
You're building a tiny game where:

The player starts with some energy.

They run, which reduces energy.

They rest, which restores energy.

You want to print the final energy.

💡 Your Goal:
Write a Python program with these functions:

run(energy) → subtract 3 from energy

rest(energy) → add 5 to energy

print_energy(energy) → prints "Final energy: X"

main() → calls run, then rest, then prints

BUT—you must write the functions in any order, as long as the program runs perfectly.
Remember: define first, execute last using main().

🔑 Rules:
Do NOT call run() or rest() before defining them.

Call main() only after everything is defined.

You must use main() as the entry point.

"""


def run(energy):
    return energy-3

def rest(energy):
    return energy+5

def print_energy(energy):
    print(f"Final energy: {energy}")

def main():
    energy = 10
    energy = run(energy)
    energy = rest(energy)
    print_energy(energy)

main()