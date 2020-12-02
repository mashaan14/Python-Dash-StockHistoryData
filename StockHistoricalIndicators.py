# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:07:27 2020

@author: mals6571
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output

# Load data
df = pd.read_csv('StockHistoryData.csv', parse_dates=True)
df['EPS'] = df.apply(lambda row: (row['Net Income']*1000) / row['Number of Shares'], axis=1)
df['Loans to Deposits Ratio'] = df.apply(lambda row: (row['Loans'] / row['Customer Deposits'])*100, axis=1)
df['Percentage of Non-performing loans'] = df.apply(lambda row: (row['Non-performing loans'] / row['Loans'])*100, axis=1)
print(df)
df.index = pd.to_datetime(df['Date'])
ColumnNames = list(df)
ColumnNames.remove('Name')
ColumnNames.remove('Date')

# Initialize the app
app = dash.Dash(external_stylesheets=[dbc.themes.SPACELAB])
# app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True


def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list

card_main = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H2('DASH - STOCK Data'),
                html.Label('Pick one or more stocks.'),
                dcc.Dropdown(id='stockselector', options=get_options(df['Name'].unique()),
                             multi=True,
                             placeholder = "Pick one or more stocks",
                             ),
            ]
        ),
    ],
)

card_Dropdown_01 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.Label('Choose the y-axis for figure 1.'),
                dcc.Dropdown(id='timeseries_01_yaxis', options=get_options(ColumnNames),
                             multi=False,
                             placeholder = "Pick the y-axis for figure 1",
                             ),
            ]
        ),
    ],
)

card_Dropdown_02 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.P('Choose the y-axis for figure 2.'),
                dcc.Dropdown(id='timeseries_02_yaxis', options=get_options(ColumnNames),
                             multi=False,
                             placeholder = "Pick the y-axis for figure 2",
                             ),
            ]
        ),
    ],
)

card_graph_01 = dbc.Card(
    dcc.Graph(id='timeseries_01', config={'displayModeBar': False})
)

card_graph_02 = dbc.Card(
    dcc.Graph(id='timeseries_02', config={'displayModeBar': False})
)


app.layout = html.Div([
    dbc.Row(dbc.Col(card_main, width=3)),
    
    dbc.Row([dbc.Col(card_Dropdown_01, width=3),
             dbc.Col(card_graph_01, width=9)]),  # justify="start", "center", "end", "between", "around"
    
    dbc.Row([dbc.Col(card_Dropdown_02, width=3),
             dbc.Col(card_graph_02, width=9)]),  # justify="start", "center", "end", "between", "around"

])

@app.callback(Output('timeseries_01', 'figure'),
              [Input('stockselector', 'value'),
              Input('timeseries_01_yaxis', 'value')])
def update_graph_01(selected_dropdown_value, yaxis_column_name):
        
    trace1 = []
    df_sub = df
    for stock in selected_dropdown_value:
        trace1.append(go.Scatter(x=df_sub[df_sub['Name'] == stock].index,
                                 y=df_sub[df_sub['Name'] == stock][df_sub.columns[df_sub.columns.get_loc(yaxis_column_name)]],
                                 mode='lines',
                                 name=stock,
                                 textposition='bottom center'))
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]        
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#ffe146", '#FF4F00', '#6aff46', '#46dfff', '#ef46ff', '#b3ff46'],
                  hovermode='x',
                  autosize=True,
                  title={'text': yaxis_column_name, 'x': 0.5},
                  xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
              ),

              }

    return figure

@app.callback(Output('timeseries_02', 'figure'),
              [Input('stockselector', 'value'),
              Input('timeseries_02_yaxis', 'value')])
def update_graph_02(selected_dropdown_value, yaxis_column_name):
        
    trace1 = []
    df_sub = df
    for stock in selected_dropdown_value:
        trace1.append(go.Scatter(x=df_sub[df_sub['Name'] == stock].index,
                                 y=df_sub[df_sub['Name'] == stock][df_sub.columns[df_sub.columns.get_loc(yaxis_column_name)]],
                                 mode='lines',
                                 name=stock,
                                 textposition='bottom center'))
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]        
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#ffe146", '#FF4F00', '#6aff46', '#46dfff', '#ef46ff', '#b3ff46'],
                  hovermode='x',
                  autosize=True,
                  title={'text': yaxis_column_name, 'x': 0.5},
                  xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
              ),

              }

    return figure

if __name__ == '__main__':
    app.run_server(debug=False)