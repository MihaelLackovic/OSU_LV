
numbers=[]
while True:
    unos = float(input())
    if unos=="Done":
        print("Gotovo")
      
    try:
        unos = float(unos)
    except:
        print("Unesi broj!")
        
    numbers.append(unos)

print("Duljina",len(numbers))
print("Minimum",min(numbers))
print("Maximum",max(numbers))
print("Prosjek",sum(numbers)/len(numbers))