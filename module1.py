
def change_frequency(frequency_changes):
    current_frequency = 0; 
    for change in frequency_changes:
        if (change[:1] == "+"):
            current_frequency = current_frequency + change[1:]
        else: 
            current_frequency = current_frequency + change[1:]
    print (str(current_frequency))

def main():
    frequency_changes = list()
    for i in range(int(input("enter the amount of changes in the frequency"))):
        frequency_changes.append(input("enter the next frequency change"))
    change_frequency(frequency_changes)
