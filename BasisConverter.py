base = int(input("Enter your base: "))
decimal = int(input("Enter your base 10 value: "))
quotient = [decimal]
remainder = [0]
output = ""
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
while quotient[len(quotient) - 1] != 0:
    remainder.append(quotient[len(quotient) - 1] % base)
    quotient.append(quotient[len(quotient) - 1] // base)
for i in range(len(remainder) - 1):
    if remainder[len(remainder) - i - 1] >= 10 and i != 0 and base > 36:
        output = "{}, ".format(output)
    if remainder[len(remainder) - i - 1] >= 10 and (11 <= base <= 36):
        remainder[len(remainder) - i - 1] = letters[remainder[len(remainder) - i - 1] - 10]
    output = "{}{}".format(output, remainder[len(remainder) - i - 1])
print("The base {} value of base 10 \"{}\" is: {}".format(base, decimal, output))
input()