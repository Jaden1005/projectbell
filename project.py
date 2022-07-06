import plotly.figure_factory as fx
import pandas as pd
import csv

df=pd.read_csv("data.csv")
fig=fx.create_distplot([df["Height(Inches)"].tolist()],["height"])
fig.show()