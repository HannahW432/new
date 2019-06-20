frequency_changes = list() 
current_frequency = 0

text_file = open('AD1P1.txt',"r")
frequency_changes = text_file.readlines()
found = False
frequencies_reached = list()
while not found: 
    for i in range(len(frequency_changes)):
        change = frequency_changes[i]
        if change[:1] == "+":
            current_frequency = current_frequency + int(change[1:])
        else: 
            current_frequency = current_frequency - int(change[1:])
        frequencies_reached.append(current_frequency)
    for x in range(len(frequencies_reached)-1):
        if frequencies_reached[x] == current_frequency:
           print(current_frequency)
           found = True
           break
text_file.close()
