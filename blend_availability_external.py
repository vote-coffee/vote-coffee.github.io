import pandas as pd
import plotly.express as px
from datetime import date

today = date.today()

df = pd.read_csv('~/Downloads/Pythoon/Green coffee timeline 2023 - Blends.csv', encoding='UTF-8')

fig = px.timeline(df, 
    x_start = "Start Date",
    x_end = "End Date",
    y = "Edition",
    text= "Edition",
    title = "Vote Coffee Blend Availability (External)", 
    hover_data = ["Coffee One", "Coffee Two", "Coffee Three"],
#    labels={"Estimated release date": "Date",  "day": "Day of Week"},
    color="Blend",
  color_discrete_map={
            "Heute": "#001a4b",
            "Morgen": "#c46c0b",
            "Gestern": "#89581f",},
#    opacity = 0.85,
    template="plotly_white",
#    height=800,
    )
fig.update_traces(visible="legendonly")
fig.data[0].visible=True

fig.update_yaxes(title='y', 
    visible=False, 
    showticklabels=True, 
    autorange="reversed")

fig.add_vline(x=today, 
    line_width=.8, 
    line_color="grey")

fig.update_layout(
    hoverlabel=dict(
        font_family="Ubuntu"
    )
)
fig.update_layout(
    font_family="Ubuntu",
    title_font_family="Ubuntu",
    font_size=13)

fig.update_xaxes(title_font_family="Ubuntu", 
    showticklabels=True, 
    side="top", 
    dtick="M1",
    tickformat="%b\n%Y")
fig.update_traces(insidetextanchor="middle")

fig.show()

fig.write_html("/home/tf/Documents/blend_availability_external.html")

