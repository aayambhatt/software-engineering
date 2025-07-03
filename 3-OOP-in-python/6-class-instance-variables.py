class Mage:
    power = 50  # 🔹 Class variable

m1 = Mage()
m2 = Mage()

m1.power = 100  # 🔸 Now this becomes an instance variable only for m1

print(m1.power)     # 100 ✅ (instance variable)
print(m2.power)     # 50 ✅ (falls back to class variable)
print(Mage.power)   # 50 ✅ (class variable stays untouched)
