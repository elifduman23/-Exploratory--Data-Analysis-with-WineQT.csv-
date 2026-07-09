import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None) # tüm kolonları gösterir
data=pd.read_csv("WineQT.csv")
print(data) # datayı yazdırır
print(data.head()) # ilk 5 satırı yazdırır
print(data.tail()) # son 5 satırı yazdırır
print(data.info) # data hakkında ilgi verir
print(data.describe()) # data daki ortalama, min - maks değer vs. konular hakkında bilgi verir
print(data.columns) # datanın kolonlarını yazdırır
print(data["quality"].unique())  # datanın "quality" kolonundaki ollan
print(data.corr(numeric_only=True))
print(data["pH"].mean()) # pH kolonunun ortalaması
print(data.isnull()) # boş olan datalara True , dolu olanlara False yazar

#matplotlib
# FREE SULFUR DİOXİDE BY TOTAL SULFUR DİOXİDE
plt.plot("free sulfur dioxide","total sulfur dioxide","y--",data=data)
plt.title("Free sulfur dioxide by total sulfur dioxide")
plt.xlabel("free sulfur dioxide")
plt.ylabel("total sulfur dioxide")
plt.show()
# scatter grafik ile
plt.scatter("free sulfur dioxide","total sulfur dioxide",data=data)
plt.title("Free sulfur dioxide by total sulfur dioxide")
plt.xlabel("free sulfur dioxide")
plt.ylabel("total sulfur dioxide")
plt.show()

# histogram grafik ile
plt.hist("total sulfur dioxide",color="red",data=data)
plt.title("total")
plt.ylabel("total sulfur dioxide")
plt.xlabel("frequency")
plt.show()

# boxplot grafik ile
plt.boxplot("total sulfur dioxide",data=data)
plt.title("total")
plt.xlabel("frequency")
plt.ylabel("total sulfur dioxide")
plt.show()

# pH BY QUALİTY and id by density
# 2 grafik ile çalışmak
# örnek 1
plt.subplot(1,2,1)
plt.scatter("pH","quality",data=data)
plt.title("pH by Quality")
plt.xlabel("pH")
plt.ylabel("Quality")

plt.subplot(1,2,2)
plt.scatter("Id","density",data=data)
plt.title("Id by density")
plt.xlabel("Id")
plt.ylabel("Density")
plt.show()

# örnek 2
plt.subplot(2,1,1)
plt.scatter("Id","sulphates",data=data)
plt.title("Sulphates")
plt.xlabel("Id")
plt.ylabel("Sulphates")
plt.subplot(2,1,2)
plt.plot("Id","quality",data=data)
plt.title("Quality")
plt.xlabel("Id")
plt.ylabel("Quality")
plt.show()

# örnek 3
# alcohol by chlorides
my_figure=plt.figure()
new_data=my_figure.add_axes([0.3,0.3,0.7,0.5])
new_data.scatter("alcohol","chlorides",data=data)
new_data.set_title("alcohol by chlorides")
new_data.set_xlabel("alcohol")
new_data.set_ylabel("chlorides")
plt.show()






