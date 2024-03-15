import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# For df_candidate
df_candidate = pd.read_csv('candidate_no_fada.csv', encoding='iso-8859-1')

print(df_candidate.head())

df = df_candidate.groupby(["Constituency", "Party Id"]).agg({"Votes": "sum"}).reset_index()

df['Vote Fraction'] = df['Votes'] / df.groupby('Constituency')['Votes'].transform('sum')

print(df.head())

urban_constituencies = [
    "Dublin Bay North", "Dublin Bay South", "Dublin Central", "Dublin Fingal", "Dublin Mid-West",
    "Dublin North West", "Dublin Rathdown", "Dublin South Central", "Dublin South West", "Dublin West",
    "Dun Laoghaire", "Cork North Central", "Cork South Central", "Limerick City"
]

mixed_constituencies = [
    "Cork East", "Cork North West", "Cork South West", "Limerick County", "Galway West",
    "Kildare North", "Kildare South", "Louth", "Waterford", "Wicklow"
]

print(len(set(df['Constituency'])))

# Adding a new column for the constituency type
df['Type'] = df['Constituency'].apply(
    lambda x: "urban" if x in urban_constituencies else ("mixed" if x in mixed_constituencies else "rural")
)

print(df.head())

# Preparing the plot data

df_pivot = df.pivot_table(index=['Constituency', 'Type'], columns='Party Id', values='Vote Fraction').reset_index()

colors = {'urban': 'red', 'rural': 'green', 'mixed': 'gray'}



# Plotting

plt.figure(figsize=(3.5, 2.5))

for ctype, group in df_pivot.groupby('Type'):
    plt.scatter(group['Fianna Fa/il'], group['Fine Gael'], color=colors[ctype], label=ctype, alpha=0.6)

plt.xlabel('FF fraction')

plt.ylabel('FG fraction')

plt.legend(loc='upper left', bbox_to_anchor=(1, 1),title='Type')
plt.tight_layout()
plt.grid(True)
plt.savefig('../02.5_ffVfg.png', dpi=300)
plt.show()
