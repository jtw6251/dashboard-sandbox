import dash
import dash_core_components as dcc
import dash_html_components as html
from utils import Header
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,  external_stylesheets=external_stylesheets)
server = app.server

COLOURS = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Brown', 'Black']

# Describe the layout/ UI of the app
app.layout = html.Div([
    Header(app),
    html.Div(
        [
            dcc.Location(id="url", refresh=False),
            html.Div(
                id="page-content",
                children=[
                    html.Br(),
                    html.Button(
                        'DO NOT PRESS',
                        className='button-primary',
                        id='clicker',
                        n_clicks=0,
                        style={'background': 'red', 'border': 'none', 'font': 'white', 'font-size': 24,
                               'height': '100px', 'width': '300px'}
                    ),
                    html.Br(),
                    html.Br(),
                    html.H4(id='button-message'),
                    html.Br(),
                    html.Br(),
                    html.H4('Select the colour to fill the box'),
                    dcc.Dropdown(
                        id='colour-dropdown',
                        options=[{'value': colour, 'label': colour} for colour in COLOURS],
                        placeholder='Select a colour...'
                    ),
                    html.Br(),
                    html.Div(
                        id='coloured-box',
                        style={'height': '250px', 'width': '500px', 'border': '1px solid black'}
                    )
                ]
            ),
        ],
        style={'padding-left': '100px', 'padding-right': '100px'}
    )
])

@app.callback(Output('button-message', 'children'),
              Input('clicker', 'n_clicks'))
def message_button_presser(n_clicks):
    if n_clicks == 0:
        raise PreventUpdate
    elif n_clicks == 1:
        return 'BOOOOOM!!!'
    elif n_clicks == 2:
        return 'You have DESTROYED the world...'
    elif n_clicks == 3:
        return 'Why are you still clicking you FOOL?!'
    else:
        return f'You refuse to give up... you\'ve clicked this button {n_clicks} times!'

@app.callback(Output('coloured-box', 'style'),
              Input('colour-dropdown', 'value'))
def return_box_styling(colour_selected):
    if colour_selected is None:
        raise PreventUpdate
    else:
        return {'height': '250px', 'width': '500px', 'border': '1px solid black', 'background': colour_selected.lower()}



if __name__ == "__main__":
    app.run_server(debug=True)