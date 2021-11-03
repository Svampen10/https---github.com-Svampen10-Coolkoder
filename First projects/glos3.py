# intorducera filen med dess namn
filename = "jabeen.txt"
#använd with istället för for 
with open (filename) as filehandle:
    line = filehandle.readline()
print(line)