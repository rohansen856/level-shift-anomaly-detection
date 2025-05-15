import pandas as pd
import plotly.graph_objects as go
from adtk.data import validate_series
from adtk.detector import LevelShiftAD
import warnings
warnings.simplefilter(action="ignore", category=UserWarning)
from level_shift_view import df, y_column



def level_shift_anomaly(series,config={'c':1,'side':'both','window':3}):
    s = validate_series(series)
    model = LevelShiftAD(c=config['c'], side=config['side'],window = config['window'])            
    anomalies = model.fit_detect(s)
    return anomalies

def _join_df_with_anomaly(df, anomalies, anomaly_column):
    anomalies = pd.DataFrame(anomalies)
    anomalies.fillna(False, inplace=True)
    anomalies.reset_index(drop=True)
    df[anomaly_column]=anomalies.to_numpy()
    return df

def plot_anomalies(df, y_column, config):
    figure = go.Figure()
    # plot baseline     
    figure.add_trace(go.Scatter(name=y_column, x = df.index, y=df[y_column], marker=dict(color='rgba(50,50,50,0.3)')))
         
    # plot anomaly points     
    anomaly_df = df
    anomaly_df = anomaly_df[anomaly_df[config['anomaly_column']]==True]
            
    figure.add_trace(go.Scatter(name=config['legend_name'], x = anomaly_df.index, y=anomaly_df[y_column], 
        mode='markers',
        marker=dict(color=config['color'],size=10)))

    figure.update_layout(
            title= 'DAU (simulated)',
            xaxis_title='date',
            yaxis_title='DAU',
            legend_title="Anomaly Type",
        )
    
    figure.show()

config={
    'anomaly_column':'levelshift_ad',
    'legend_name': 'levelshift anomaly',
    'color':'rgba(249,123,34,0.8)'
}

anomalies = level_shift_anomaly(df)
df_anomalies = _join_df_with_anomaly(df,anomalies,config['anomaly_column'])
plot_anomalies(df_anomalies,y_column,config)