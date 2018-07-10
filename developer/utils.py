import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import io



def scatterplot(x, y):
    "return buffer in-memory of .png scatterplot"
   _x_= x['Value']
   _y = y['Value']

   fig, ax = plt.subplots(figsize=(10, 5))

   #assigns a color to each data point
   colors = ['#2300A8', '#00A658']

   #iterates through the dataset plotting each data point and assigning it its corresponding color and label
   for i in range(len(_x)):
     ax.scatter(_x[i], _y[i], alpha=0.70, color = colors[i%len(colors)])

   #adds title and axes labels
   ax.set_title('ScatterPlot')
   ax.set_xlabel(x.__dict__['_name'])
   ax.set_ylabel(y.__dict__['_name'])

   #removing top and right borders
   ax.spines['top'].set_visible(False)
   ax.spines['right'].set_visible(False)

   #adds major gridlines
   ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

   buf = io.BytesIO()
   ax.savefig(buf, format='png')
   buf.seek(0)

   return buf



