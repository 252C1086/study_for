import pandas as pd
import numpy as np

path = "C:/Users/aeijn/study_for_intern/stu_python/file_controll/"

data = {
    "name":["田中", "佐藤", "鈴木", "山田", "伊藤"],
    "department":["開発", "営業", "開発", "営業", "開発"],
    "age":[22, 25, 28, 21, 24],
    "salary":[280000, 310000, 350000, 260000, 300000]
}

df = pd.DataFrame(data)
df1 = df.query("age >= 25")
df1.to_csv(path + "data1.csv", index=False)
df2 = df.sort_values(by="salary", ascending=False)
df2.to_csv(path + "data2.csv",index=False)
df3 = df.groupby(by="department")["salary"].mean()
df3.to_csv(path + "data3.csv")
df4 = df3.sort_values(ascending=False)
df4.to_csv(path + "data4.csv")
