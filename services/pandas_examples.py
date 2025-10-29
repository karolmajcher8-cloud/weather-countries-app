import pandas as pd

df = pd.read_excel("Financial Sample.xlsx")


# podgląd danych
pd1 = df.head() # pierwsze 5 wierszy
pd2 = df.tail(3)
pd3 = df.shape
pd4 = df.columns
pd5 = df.dtypes
pd6 = df.describe()
# print(pd6)

# Średnia wybranych kolumn

pd7 = df[" Sales"].mean() #Średnia dla kolumny
pd8 = df[[" Sales" , "Profit"]].mean()
pd9 = df.loc[0:2] #wybór wierszy
pd10 = df.loc[20:30, ["Country", "Product", " Sales"]]
# print(pd10)
# Filtrowanie rekordów

pd11 = df[ df[" Sales"] > 50000]
pd12 = df[df["Country"] == "France"]

# #Sposób 1
# pd13 = df[(df[" Sales"] > 50000) & (df["Country"] == "France") ]
#
# #sposób 2
# pd14 = df.loc[mask]
# pd15 = df.loc[mask, ["Country","Product"," Sales"]]

# Sortowanie
# pd16 = (df.sort_values(by=[" Sales"]))
# pd17 = df.loc[pd16, ["Country"," Sales"]]
pd18 = df.sort_values(by=["Units Sold"], ascending=[False]).head(5)

# print(pd18)
#
# # Nowa kolumna
# df["MarginPercent"] = df["Profit"] / df[" Sales"]
# df["Testowa"] = "Testowy napis"
#
# pd19 = df.loc[0:20, ["Product","MarginPercent","Testowa"]]

min_profit = df['Profit'].min()
print(min_profit)