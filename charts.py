import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


data = pd.read_csv('stargravityfinal.csv')



planet_name = []
planet_distance = []
planet_mass = []
planet_radius = []
planet_gravity = []

for p in data:
  planet_name.append(p[1])
  planet_distance.append(p[2])
  planet_mass.append(p[3])
print(p)
fig1 = px.bar(x= planet_name, y= planet_distance, labels={'x':'Star Name', 'y':'Light Years'})
fig1.show()
fig2 = px.bar(x= planet_name, y= planet_mass, labels={'x':'Star Name', 'y':'Mass'})
fig2.show()
fig3 = px.bar(x= planet_name, y= planet_radius, labels={'x':'Star Name', 'y':'Radius'})
fig3.show()
fig4 = px.bar(x= planet_name, y= planet_gravity, labels={'x':'Star Name', 'y':'Gravity'})
fig4.show()