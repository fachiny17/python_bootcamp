from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikatchi","Mkpamkpab","Lopikop"])
table.add_column("Type",["Electric","Marrr","Ciopoi"])

table.align = "l" #left alignment

print(table)