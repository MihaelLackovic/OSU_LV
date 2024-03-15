song = open ("song.txt")
rijeci={}
count=0

for line in song :
    line = line.rstrip()
    words =line.split()
    for word in words:
        if word in rijeci:
            rijeci[word] += 1
        else:
            rijeci[word] = 1
    
print(rijeci)


for word in rijeci:
    if rijeci[word] == 1:
        print(word)
        count += 1

print(count)

song.close()