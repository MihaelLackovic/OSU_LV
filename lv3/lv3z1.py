import pandas as pd

data = pd.read_csv("data_C02_emission.csv")


print("a)")
print("Tipovi podataka", data.dtypes)
print("Broj mjerenja", data.__len__())
print("Postojanje dupliciranih vrijednosti", len(data.isnull()))
data.drop_duplicates()

data["Make"] = data["Make"].astype("category")
data["Model"] = data["Model"].astype("category")
data["Vehicle Class"] = data["Vehicle Class"].astype("category")
data["Transmission"] = data["Transmission"].astype("category")
data["Fuel Type"] = data["Fuel Type"].astype("category")
data["Engine Size (L)"] = data["Engine Size (L)"].astype("int64")


print("b)")
print("Najveća potrošnja:", data.sort_values(by=["Fuel Consumption City (L/100km)"]).tail(3)[["Make","Model", "Fuel Consumption City (L/100km)"]])
print("Najmanja potrošnja:", data.sort_values(by=["Fuel Consumption City (L/100km)"]).head(3)[["Make","Model", "Fuel Consumption City (L/100km)"]])


print("c)")
print("Vozila sa veličinom motora izmedu 2.5L i 3.5L", data[(data["Engine Size (L)"] > 2.5) & (data["Engine Size (L)"] < 3.5)].__len__()) 
print("\nProsječna a C02 emisija plinova: ", data[((data["Engine Size (L)"] > 2.5) & (data["Engine Size (L)"] < 3.5))]["CO2 Emissions (g/km)"].mean())


#print("d)")
#print("Audi sa 4 cilindra",data[data["Model"]=="audi"].__len__,data[(data["Model"]=="Audi") & (data["Cylinders"]==4)]["CO2 Emissions (g/km)"].mean())


print("e)")  
print("Broj vozila s obzirom na broj cilindara: ", data.groupby("Cylinders").size())
print("Prosječna emisija C02 sa obzirom na broj cilindara", data.groupby("Cylinders")["CO2 Emissions (g/km)"].mean())
print("Medijan co2 s obzirom na broj cilindara ", data.groupby("Cylinders")["CO2 Emissions (g/km)"].median())


print("f)")
print("Dizel:gradska potrošnja ", data[data["Fuel Type"] == "D"]["Fuel Consumption City (L/100km)"].mean())
print("Benzin:gradska potrošnja", data[data["Fuel Type"] == "X"]["Fuel Consumption City (L/100km)"].mean())
print("Dizel:median potrošnja", data[data["Fuel Type"] == "D"]["Fuel Consumption City (L/100km)"].median())
print("Benzin:median potrošnja", data[data["Fuel Type"] == "X"]["Fuel Consumption City (L/100km)"].median())


print("g")
print("Dizeli sa 4 cilindra s najvećom potrošnjom ", data[(data["Cylinders"] == 4) & (data["Fuel Type"] == "D")].sort_values(by=["Fuel Consumption City (L/100km)"], ascending=False).head(1))


print("h)")
print("Ručni mjenjač ", data[data["Transmission"].str.startswith("M")].__len__())


print("i)")
print("Korelacija: ", data.corr(numeric_only=True))
