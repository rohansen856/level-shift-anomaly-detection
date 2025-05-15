import pandas as pd
import plotly.graph_objects as go

def load_data(filename,x_column,y_column):
    df = pd.read_csv(filename)
    df.index = pd.to_datetime(df[x_column])
    df.drop(columns=x_column,inplace=True)
    df[y_column] = df[y_column].astype(float)
    return df

def plot_base_line(df,y_column):
    figure = go.Figure()
    figure.add_trace(go.Scatter(name=y_column, x = df.index, y=df[y_column], marker=dict(color='rgba(50,50,50,0.3)')))
    figure.show()