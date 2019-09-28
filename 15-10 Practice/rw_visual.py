import plotly.graph_objects as go
from plotly import offline
from random_walk import RandomWalk
import numpy as np

rw = RandomWalk()
rw.walk()

fig = go.Figure(data=go.Scatter(
    y=rw.y_values,
    x=rw.x_values,
    mode='markers',
   )
)
fig.update_layout(title="Path taken starting at (0,0)")
offline.plot(fig, filename='randomwalk.html')



