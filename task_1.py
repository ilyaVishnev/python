from sys import argv

script_name, hours, earning_per_hour, bonus = argv
print("your salary -> " + str(int(hours) * int(earning_per_hour) + int(bonus)))
