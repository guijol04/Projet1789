
liste = []
file = open("noms.txt", "r")
output = open("nomstitled.txt", "a")
for line in file:
    output.write(str(line).title())
file.close()
output.close()