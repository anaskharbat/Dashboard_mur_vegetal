import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import datetime

app = dash.Dash(__name__)
temperature_value = str(15) + ' Degrés'
humidity_value = str(80)  +  " \r% d\' humidité"
battery_value = str(90) + " \r% de batterie"
CO2_value = str(10) + ' Grammes'
O2_value = str(5) + ' Grammes'
water_value = str(50) + ' Litres'
pollution_value = str(100) + ' Grammes'
time_value = datetime.datetime.now().strftime('%d-%m-%Y') + ' ' +  datetime.datetime.now().strftime('%H:%M:%S')
app.layout = html.Div([

    html.Div(id="time",children = html.P(time_value)),

    html.Div(id='left-block',children = [
        html.Div(id='temperature-block',children=
        [
            html.Div(id='temperature-value',children=
                html.P(temperature_value)
            ),
            html.Div(id='temperature-img',children=
                html.Img(src='/assets/img/thermometer.jpg')
            )

        ]),

        html.Div(id='humidity-block',children=
        [
            html.Div(id='humidity-value',children=
                html.P(humidity_value)
            ),
            html.Div(id='humidity-img',children=
                html.Img(src='/assets/img/water_drop.png')
            )

        ]),

        html.Div(id='battery-block',children=
        [
            html.Div(id='battery-value',children=
                html.P(battery_value)
            ),
            html.Div(id='battery-img',children=
                html.Img(src='/assets/img/battery-symbol.jpg')
            )

        ]),
    ]),

    html.Div(id='right-block',children=
        html.Div(id='wall-container',children=[
        html.Div(id='img-wall', children=html.Img(src='/assets/img/wall.jpeg')),
        html.Div(id='mapping-wall', children=[ 
            html.Div(id='left-wall',children=[
                html.Div(id='column-0',children=[
                    html.Div(id='cell-0',children=[
                        html.P(0)
                    ]),
                    html.Div(id='cell-1',children=[
                        html.P(1)
                    ]),
                    html.Div(id='cell-2',children=[
                        html.P(2)
                    ])
                ]),
                html.Div(id='column-1',children=[
                    html.Div(id='cell-3',children=[
                        html.P(3)
                    ]),
                    html.Div(id='cell-4',children=[
                        html.P(4)
                    ]),
                    html.Div(id='cell-5',children=[
                        html.P(5)
                    ])

                ]),
                html.Div(id='column-2',children=[
                    html.Div(id='cell-6',children=[
                        html.P(6)
                    ]),
                    html.Div(id='cell-7',children=[
                        html.P(7)
                    ]),
                    html.Div(id='cell-8',children=[
                        html.P(8)
                    ])

                ])
            ]),
            html.Div(id='right-wall',children=[
                html.Div(id='column-3',children=[
                    html.Div(id='cell-9',children=[
                        html.P(9)
                    ]),
                    html.Div(id='cell-10',children=[
                        html.P(10)
                    ]),
                    html.Div(id='cell-11',children=[
                        html.P(11)
                    ])
                ]),
                html.Div(id='column-4',children=[
                    html.Div(id='cell-12',children=[
                        html.P(12)
                    ]),
                    html.Div(id='cell-13',children=[
                        html.P(13)
                    ]),
                    html.Div(id='cell-14',children=[
                        html.P(14)
                    ])

                ]),
                html.Div(id='column-5',children=[
                    html.Div(id='cell-15',children=[
                        html.P(15)
                    ]),
                    html.Div(id='cell-16',children=[
                        html.P(16)
                    ]),
                    html.Div(id='cell-17',children=[
                        html.P(17)
                    ])

                ])
            ]),
        ]) 
    ])

    ),
    html.Div(id='footer', children= [
        html.Div(id="CO2",children=html.P(CO2_value)),
        html.Div(id="O2",children=html.P(O2_value)),
        html.Div(id="Water",children=html.P(water_value)),
        html.Div(id="pollution",children=html.P(pollution_value)),
        html.Div(id='logo', children=html.Img(src='/assets/img/image.png'))   
    ]),

])

if __name__ == '__main__':
    app.run_server(debug=True)