import pandas as pd
from pandas.tools.plotting import parallel_coordinates
from matplotlib import pyplot as plt

data = pd.read_csv('fortune500_data.csv')

# print df.head()


# pivot df
# df = df.pivot(index='Company', columns='Year', values='Rank')


df = pd.pivot_table(data, values='Rank', index='Company', columns='Year').reset_index()

df = df.sort_values(by=[2005]).reset_index()

i_filter = range(0, 100)
j_filter = range(1995, 2006)
j_filter.append('Company')

print j_filter
print i_filter


df = df.loc[i_filter, j_filter]


print df.head()

plt.figure(figsize=(10, 10))
parallel_coordinates(df, 'Company')
plt.ylim(50, 1)


plt.xlabel('Year')
plt.ylabel('Rank')
plt.title('Current Top 100 Fortune500 Companies')
plt.legend(bbox_to_anchor=(0.90, 0.4), loc=2, borderaxespad=0.)
plt.show()
