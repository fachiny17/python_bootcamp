from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Monday",["Wake","Pray","Eat"])
table.add_column("Tuesday",["Dream","Practice","Observe"])
table.add_column("Wednesday",["Organise","Play","Grind"])

print(table)