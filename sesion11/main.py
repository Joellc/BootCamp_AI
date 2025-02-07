import pandas as pd
paht = "Online_Retail.csv"

retail_data = pd.read_csv(paht, encoding='latin1')

print(type(retail_data))
print(retail_data)