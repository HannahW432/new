
text_file = open("AD3.txt", "r")
claims = text_file.readlines()
locations = []
for elfclaim in claims:
    horiz = int(elfclaim[elfclaim.find("@ ")+2:elfclaim.find(",")])
    vertical = int(elfclaim[elfclaim.find(",")+1:elfclaim.find(":")])
    width = int(elfclaim[elfclaim.find(": ")+2:elfclaim.find("x")])
    length = int(elfclaim[elfclaim.find("x")+1:len(elfclaim)])
    for r in range(length):
        for w in range(width):
            locations.append((1000 * r) + horiz + w)
print(len(locations))
t = []
for i in locations: 
    if i not in t: 
        t.append(i)
    elif i in t:
        t.remove(i)
print(len(t))
print(len(locations) - len(t)) 
