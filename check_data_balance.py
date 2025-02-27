import pandas as pd

data = pd.read_csv("health_data.csv")
print(data["high_risk"].value_counts())
