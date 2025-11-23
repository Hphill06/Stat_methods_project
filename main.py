import pandas as pd

df = pd.read_csv('all_pokemon_data.csv')



print("*** Variances ***")

variances = df.groupby('Primary Typing')['Base Stat Total'].var(ddof=1).sort_values(ascending=False)

std_devs = df.groupby('Primary Typing')['Base Stat Total'].std(ddof=1).sort_values(ascending=False).sort_values()


print(round(std_devs,2))
