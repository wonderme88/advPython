import numpy as np
import pandas as pd

# https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html

#object creation, creating series by passing list of values
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

#creating Dataframe by passing a numpy array, with datetime index and labeled columns

dates = pd.date_range("20210101", periods=6)
print(dates)

#Dataframes
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)


#Creating DataFrame by passing a dict of objects that can be converted to series like.
df2 = df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2)
print(df2.dtypes)



print(df.head)
print(df.tail)
print(df.index)
print(df.columns)


print(df.to_numpy())
print(df2.to_numpy())
print(df.describe)
print(df.sort_index(axis=1, ascending=False))
print(df.sort_values(by="B"))
print(df["A"])


#Grouping

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
print(df)
print(df.groupby("A").sum())
print(df.groupby(["A","B"]).sum())


