import pandas as pd
df = pd.read_csv("customer_shopping_data.csv")

df["total_amount"] = df["quantity"] * df["price"]
print(df.head())

print(df["customer_id"].nunique())

print(df.sort_values("total_amount", ascending=False)
[["customer_id", "total_amount"]].head())

print(df["customer_id"].value_counts().head())

print(df.sort_values("total_amount", ascending=False)
[["category", "total_amount"]].head())

print(df["category"].value_counts().head())

print(df.sort_values("total_amount",ascending=False)
[["gender", "total_amount"]].head())

print(df["gender"].value_counts())


df["customer_type"] = "Low"

df.loc[df["total_amount"] > 20000, "customer_type"] = "High"

df.loc[(df["total_amount"] > 10000) & (df["total_amount"] <= 20000), "customer_type"] = "Medium"

print(df[["total_amount", "customer_type"]].head())

print(df["customer_type"].value_counts())