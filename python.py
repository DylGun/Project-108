import pandas as pd
import plotly.figure_factory as ff
import csv
data1=pd.read_csv("data9.csv")
data2=ff.create_distplot([data1["Avg Rating"].tolist()],["Avg Rating"])
data2.show()