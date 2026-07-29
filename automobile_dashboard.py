import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

df = pd.read_csv('automobile_sales.csv')

app = dash.Dash(__name__)

dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]

year_list = [i for i in range(1980, 2024)]
app.layout = html.Div([
    html.H1("Automobile Sales Statistics Dashboard",
            style={'text-align':'center', 'color':'#503D36', 'font-size':24}),
    html.Div([
        html.Label('Select Statistics'),
        dcc.Dropdown(
                 id='dropdown-statistics',
                 options=[
                     {'label':'Yearly Statistics', 'value':'Yearly Statistics'},
                     {'label':'Recession Period Statistics', 'value':'Recession Period Statistics'}
                 ],
                 placeholder='Select a report type',
                 value='Select Statistics',
                 style={'width':'80%', 'padding':'3px', 'font-size':'20px', 'text-align':'center'}
        ),
        dcc.Dropdown(
            id='select-year',
            options=[{'label':i, 'value':i} for i in year_list],
            value='Select-year',
            placeholder='Select-year',
        )

    ]),
    html.Div([
        html.Div(id='output-container', className='chart-grid', style={'display':'flex', 'flex-direction':'column'})
    ]),
])

@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics', component_property='value')
)

def update_input_cont(selected_statistics):
    if selected_statistics == 'Yearly Statistics':
        return False
    else:
        return True

@app.callback(
    Output(component_id='output-container', component_property='children'),
    [
        Input(component_id='select-year', component_property='value'),
        Input(component_id='dropdown-statistics', component_property='value')
    ]
)

def update_output_container(input_year, selected_statistics):
    if selected_statistics == 'Recession Period Statistics':
        recession_data = df[df['Recession'] == 1]
    #plot1: automobile slaes fluctuation over recession period (year-wise)
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        chart1 = dcc.Graph(
            figure=px.line(yearly_rec, 
                           x='Year', y='Automobile_Sales', 
                           title='Average Automobile Sales Fluctuation over Recession Period')
        )
    #plot2: Average number of vehicles sold by vehicle type
        avg_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        chart2 = dcc.Graph(
            figure=px.bar(avg_sales,
                          x='Vehicle_Type',
                          y='Automobile_Sales',
                          title='Average Number of Vehicles Sold per Vehicle Type during Recession Periods')
        )

    #plot3: pie chart for the total expenditure share by vehicle type
        avg_exp = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].mean().reset_index()
        chart3 = dcc.Graph(
            figure=px.pie(avg_exp, 
                          values='Advertising_Expenditure', 
                          labels='Vehicle_Type',
                          title='Total Advertising Expenditure per Vehicle Type during Recession Periods')
        )

    #plot4: effect of unemployment rate on vehicle type and sales
    #grouping data for plotting
        unemp_sales = recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        chart4 = dcc.Graph(
            figure=px.bar(unemp_sales,
                          x='unemployment_rate',
                          y='Automobile_Sales',
                          color='Vehicle_Type',
                          labels={'unemployment_rate': 'Unemployment Rate', 'Automobile_Sales': 'Average Automobile Sales'},
                          title='Effect of Unemployment Rate on Vehicle Type and Sales')
        )

        return [
            html.Div(className='chart-item', children=[
                html.Div(children=chart1),
                html.Div(children=chart2)
            ], style={'display':'flex'}),
            html.Div(className='chart-item', children=[
                html.Div(children=chart3),
                html.Div(children=chart4)
            ], style={'display':'flex'}
            )
        ]

    elif (input_year and selected_statistics == 'Yearly Statistics'):
        yearly_data = df[df['Year'] == input_year]

        #plot1: yearly sales for the whole period
        year_sales = df.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Ychart1 = dcc.Graph(
            figure=px.line(
                year_sales,
                x='Year',
                y='Automobile_Sales',
                markers=True,
                title='Total Yearly Automobile Sales'
            )
        )

        #plot2: monthly automobile sales
        monthly_sales = df.groupby('Month')['Automobile_Sales'].mean().reset_index()
        Ychart2 = dcc.Graph(
            figure=px.line(
                monthly_sales,
                x='Month',
                y='Automobile_Sales',
                title='Total Monthly Automobile Sales'
            )
        )

        #plot3: average vehicles sold during the given year
        avg_data = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Ychart3 = dcc.Graph(
            figure=px.bar(
                avg_data,
                x='Vehicle_Type',
                y='Automobile_Sales',
                title=f'Average Number of Cars Sold per Vehicle Type in the year {input_year}'
            )
        )

        #plot4: total advertisement expenditure for each vehicle
        ads_vehicle = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].mean().reset_index()
        Ychart4 = dcc.Graph(
            figure=px.pie(
                ads_vehicle,
                values='Advertising_Expenditure',
                names='Vehicle_Type',
                title=f'Advertising Expenditure per Vehicle Type in the Year {input_year}'
            )
        )

        return [
            html.Div(className='chart-item', children=[
                html.Div(children=Ychart1),
                html.Div(children=Ychart2)
            ], style={'display':'flex'}
            ),
            html.Div(className='chart-item', children=[
                html.Div(children=Ychart3),
                html.Div(children=Ychart4)
            ], style={'display':'flex'}
            )
        ]

    else:
        return None


if __name__ == '__main__':
    app.run(debug=True)