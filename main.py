import pandas as pd
import scipy.stats as stats
import math

df = pd.read_csv("all_pokemon_data.csv")



print("*** Variances ***")

variances = round(df.groupby("Primary Typing")["Base Stat Total"].std(ddof=1).sort_values(ascending=False),2)
means = round(df.groupby("Primary Typing")["Base Stat Total"].mean().sort_values(ascending=False),2)

summary_table = pd.DataFrame({
    "Mean BST": means,
    "Var": variances
})

print(summary_table)

top = variances.index[0]

print(f"\ntop variance: {top}")

#ftest to compare variance of top variance compared to rest

topVar = df[df["Primary Typing"] == top]["Base Stat Total"]
restVar = df[df["Primary Typing"] != top]["Base Stat Total"]

s21 = topVar.var(ddof=1)
s22 = restVar.var(ddof=1)

fstat = s21 / s22


df1 = len(topVar) - 1
df2 = len(restVar) - 1

p_value = 1 - stats.f.cdf(fstat, df1, df2)

print(f"Variance ({top}): {math.sqrt(s21):.2f}")
print(f"Variance (Rest):    {math.sqrt(s22):.2f}")
print(f"F-Statistic:        {fstat:.6f}")
print(f"P-Value:            {p_value:.6f}")

'''

null hyp :highest_var == rest_var
hyp a : highest_var > rest_var <- this one is true

we now know that psychic pokemon are more variable than the rest, and have a wider range of values compared to the rest of the pokemon types

'''