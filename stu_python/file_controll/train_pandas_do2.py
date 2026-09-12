from pathlib import Path
import pandas as pd

myPath = Path("C:/Users/aeijn/study_for_intern/stu_python/file_controll/")

target_dir = Path("./sales")
df_list = [pd.read_csv(f) for f in target_dir.rglob("*.csv")]
df = pd.concat(objs=df_list, axis=0, ignore_index=True, join="outer")

df["sales"] = df["quantity"] * df["price"]
df_ranling = df.sort_values("sales")

df1 = df.groupby("product").agg({"sales": "sum"}).sort_values("sales", ascending=False)
df1.to_csv(myPath / "result.csv")



