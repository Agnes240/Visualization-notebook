# -*- coding: utf-8 -*-
# Displaying different visualizations using python
#barplot
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
sns.barplot(x = 'time',y = 'total_bill',data = df)
plt.show()

#Barchart
import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')
fig.show()

#Barplot
import pandas as pd

plotdata = pd.DataFrame({

    "2021":[57,67,77,83],

    "2022":[68,73,80,79],

    "2023":[73,78,80,85]},

    index=["Laptops", "Phones", "TV's", "Sound systems"])
plotdata.plot(kind="bar",figsize=(5, 5))

plt.title("Product ratings")

plt.xlabel("Products")

plt.ylabel("Ratings")

#Creating line graphs

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
car= np.array(["Audi","Tesla","Jeep","Subaru","BMW","Forester"])
weight= np.array([0.48, 1.75, 2.9, 2.5, 3.0, 3.3])

#Using a line plot
#plt.plot(car,weight)

#using a scatter plot
#plt.scatter(car, weight)

#using a bar graph and setting different color sizes
plt.bar(car, weight, color=['black','yellow','blue', 'green', 'purple','red'])
plt.title("Weight of different cars")
plt.xlabel("Car Models")
plt.ylabel("Weight in Tonnes")
plt.show()

#Scatter plots
import numpy as np
import matplotlib.pyplot as plt

car = np.array(["Caterham", "Tesla", "Audi",  "BMW", "Ford", "Jeep"])
weight = np.array([0.48, 1.7, 2, 2, 2.3, 3 ])

# set colors and sizes
colors = np.array([0, 1, 2, 3, 4, 5])
sizes = np.array([20, 40, 60, 80, 100, 120])

plt.scatter(car, weight, c=colors, s=sizes, marker='*')
plt.show()

#Barplot while setting the colors individually
from matplotlib import pyplot as plt

bars = plt.bar([1, 2, 3, 4], [1, 2, 3, 4])
bars[0].set_color('green')
bars[1].set_color('black')
bars[2].set_color('red')
plt.show()

#Paiplots
# importing packages
import seaborn
import matplotlib.pyplot as plt

# loading dataset using seaborn
df = seaborn.load_dataset('tips')
# pairplot with hue sex
seaborn.pairplot(df, hue ='sex')
# to show
plt.show()

import pandas as pd
import plotly.express as px

# Creating the dataframe
df = pd.DataFrame({
    'Devices': ['Smartphone', 'Laptop', 'Earphones'],
    'Supplier1': [60000, 50000,  1000],
    'Supplier2': [70000, 20000, 500],
    'Suplier3': [100000, 60000, 2000.]
})

# Melt the dataframe for Plotly
melted_df = pd.melt(df, id_vars=['Devices'], var_name='Supplier', value_name='Amount in ksh')

# Create the column chart using Plotly
fig = px.bar(melted_df, x='Devices', y='Amount in ksh', color='Supplier',
             labels={'Amount in ksh': 'Amount in ksh'},
             title='Supplier-wise Price Analysis for Electronic Devices',
             barmode='group', # Use 'barmode' to display multiple bars per month,
            text_auto = True)

# Set x-axis title
fig.update_xaxes(title='Devices')

# Show the plot
fig.show()
