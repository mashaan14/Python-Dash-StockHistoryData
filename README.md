# Visualize Stock's History Indicators Using Dash in Python

This Python code creates a web application using Dash library. The web application displays two line graphs for indicators of the selected stocks. There are three stocks:
1. [National Commercial Bank (NCB)](https://www.tadawul.com.sa/wps/portal/tadawul/market-participants/issuers/issuers-directory/company-details/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zi_Tx8nD0MLIy83V1DjA0czVx8nYP8PI0MDAz0I4EKzBEKDEJDLYEKjJ0DA11MjQzcTfXDCSkoyE7zBAC-SKhH/?companySymbol=1180).
2. [Al Rajhi Bank (ALRAJHI)](https://www.tadawul.com.sa/wps/portal/tadawul/market-participants/issuers/issuers-directory/company-details/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zi_Tx8nD0MLIy83V1DjA0czVx8nYP8PI0MDAz0I4EKzBEKDEJDLYEKjJ0DA11MjQzcTfXDCSkoyE7zBAC-SKhH/?companySymbol=1120)
3. [Riyad Bank (RIBL)](https://www.tadawul.com.sa/wps/portal/tadawul/market-participants/issuers/issuers-directory/company-details/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zi_Tx8nD0MLIy83V1DjA0czVx8nYP8PI0MDAz0I4EKzBEKDEJDLYEKjJ0DA11MjQzcTfXDCSkoyE7zBAC-SKhH/?companySymbol=1010)

The history indicators cover 15 quarters from 3/31/2017 to 9/30/2020. The indicators are:
* Net Income,
* Number of Shares,
* Total Assets,
* Shareholders Equity,
* Loans,
* Customer Deposits,
* Non-performing loans

The codes calculates the following indicators:
* EPS
* Loans to Deposits Ratio
* Percentage of Non-performing loans 

## Installation

To run this code, the following packages has to be installed:
```python
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
```

## Usage

Run the code in Python, then open this address (http://127.0.0.1:8050/) in your browser to play with the web application.


## Output

<p align="center">
  <img width="1200" src=Capture.PNG>
</p>

## Disclaimer

This code was designed for educational purposes only. It is provided as is with no warranty. The stocks' history indicators were copied from TADAWUL website manually, and there's a high chance that I made a mistake while copying the data.
