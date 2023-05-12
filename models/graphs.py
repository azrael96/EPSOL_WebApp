#Import the necessary libraries
import json
import plotly
import pandas as pd
import plotly.express as px

#Genereate the graph
def giveGraph(data):
    # main variables to graph
    unixtime = []
    datos = []

    # trasform enter data
    for row in data:
        unixtime.append(row[0])
        datos.append(row[1])

    # create a dataframe
    df = pd.DataFrame({
        'unixtime': unixtime,
        'datos': datos,
    })
    df = df.sort_values(by="unixtime")
    df['unixtime'] = pd.to_datetime(df['unixtime'], unit='s')

    # create the graph
    fig = px.line(df, x='unixtime', y='datos')

    #trasform into json
    dat = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return dat
