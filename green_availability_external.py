import pandas as pd
import plotly.express as px
from datetime import date

today = date.today()

df = pd.read_csv('~/Downloads/Pythoon/Green coffee timeline 2023 - All info.csv', encoding='UTF-8')

fig = px.timeline(df, 
    x_start = "Estimated release date",
    x_end = "Estimated end date",
    y = "Name",
    text= "Name",
    title = "Vote Coffee Green Availability (External)", 
#   labels={"Estimated release date": "Date",  "day": "Day of Week"},
    hover_data = ["Importer", "Harvest Year", "Price green (€/kg)", "Price wholesale", "Description"],
    color="Range",
       color_discrete_map={
            "Süß & Einfach": "#CC6600",
            "Favourites": "#003399",
            "Blend Component Only": "#009933",
            "Etwas Besonderes": "#CC66CC"},
#    color_discrete_sequence=px.colors.qualitative.Prism,
    template="plotly_white",
#   opacity = 0.85,
#   height=800,
    )
fig.update_traces(visible="legendonly")
fig.data[0].visible=True

fig.update_yaxes(title='y', 
    visible=False, 
    showticklabels=True, 
    autorange="reversed")

fig.update_xaxes(title_font_family="Ubuntu", 
    showticklabels=True, 
    side="top", 
    dtick="M1",
    tickformat="%b\n%Y")

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

fig.update_traces(insidetextanchor="middle")

fig.show()

fig.write_html("/home/laurel/Downloads/Pythoon/green_availability_external.html")
