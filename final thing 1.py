import pandas
import seaborn
import matplotlib.pyplot as plt



data_2016 = pandas.read_csv("2016.csv")
data_2020 = pandas.read_csv("2020.csv")

data_2016.drop(data_2016.columns.difference(["committee_name", "contributor_name"]), 1, inplace=True)
data_2020.drop(data_2020.columns.difference(["committee_name", "contributor_name"]), 1, inplace=True)

data_joined = data_2016.merge(right = data_2020, on = "contributor_name", how = "inner")
data_joined.rename(columns={"committee_name_x": "committee_name_2016", "committee_name_y": "committee_name_2020"}, inplace=True)

print(data_joined.head())


plot1 = seaborn.displot(data_joined, x = "committee_name_2016", y = "committee_name_2020")
plt.show()