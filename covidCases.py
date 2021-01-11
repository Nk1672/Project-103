import pandas as pd

import plotly.express as px

df = pd.read_csv("C:/NIRVIK/Python_Whitehatjr/Projects/Project 103/cases.csv")

fig = px.line(df, x="Date", y="Number of cases", color="Country", title='COVID-19 Cases in Countries')

fig.show()