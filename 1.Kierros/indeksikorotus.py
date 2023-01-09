benefits = float(input("Enter the amount of the study benefits: "))
index = 1.0117
newBenefits = benefits * index


print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be", newBenefits, "euros")

newBenefits = newBenefits * index

print("and if there was another index raise, the study")
print("benefits would be as much as", newBenefits, "euros")
