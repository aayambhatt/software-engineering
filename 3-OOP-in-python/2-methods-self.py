class Soldier:
    health = 100

    def take_damage(self, damage, multiplier):
        # "self" is dalinar in the first example
        #
        damage = damage * multiplier
        self.health -= damage

dalinar = Soldier()
# "damage" and "multiplier" are passed explicitly as arguments
# 20 and 2, respectively
# "dalinar" is passed implicitly as the first argument, "self"
dalinar.take_damage(20, 2)
print(dalinar.health)
# 60

adolin = Soldier()
# Again, "adolin" is passed implicitly as the first argument, "self"
# "damage" and "multiplier" are passed explicitly as arguments
adolin.take_damage(10, 3)
print(adolin.health)
# 70

print(Soldier.health)
#100