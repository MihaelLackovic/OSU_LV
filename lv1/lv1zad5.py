sms = open("SMSSpamCollection.txt")

spamCounter=0
hamCounter=0
usklicnikCounter=0
spamWordLenght=0
hamWordLenght=0

for line in sms:
    if(line.startswith("ham")):
        hamCounter=hamCounter+1
        hamWordLenght=hamWordLenght+len(line.split()[1::])
        
    if(line.startswith("spam")):
        spamCounter=spamCounter+1
        spamWordLenght=spamWordLenght+len(line.split()[1::])
        if(line.endswith("!")):
            usklicnikCounter=usklicnikCounter+1


print("Prosjecan broj rjeci u hamu je:",float(hamWordLenght/hamCounter))
print("Prosjecan broj rjeci u spamu je:",float(spamWordLenght/spamCounter))
print(usklicnikCounter)ž





