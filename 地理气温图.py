import pandas as pd
data = {
    "month":[1,2,3,4,5,6,7,8,9,10,11,12],
    "temp":[2,4,9,16,22,27,30,29,24,18,10,4],
    "rain":[30,40,55,70,90,120,160,140,80,60,45,35]
}
df=pd.DataFrame(data)
print(df)
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df["temp"].mean())
print(df["temp"].max())
print(df["rain"].sum())
print(df["temp"].idxmax())
hot_month= df.loc[df["temp"].idxmax(),"month"]
print(f"最热的月份是{hot_month}月")
import matplotlib.pyplot as plt
plt.plot(df["month"],df["temp"],marker="o")
plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature(C)")
plt.grid(True)
plt.savefig("temp.png",dpi=150)
plt.show()
