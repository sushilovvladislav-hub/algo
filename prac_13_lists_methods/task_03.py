print("Программа разбивает путь Windows на части по символу \\")

path = input("Введите путь (пример C:\\Windows\\System32\\calc.exe): ")
path_parts = path.split("\\")

print(*path_parts, sep="\n")
