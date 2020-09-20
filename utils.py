import dash_html_components as html
import dash_core_components as dcc
import base64

image_filename = 'assets/quavers.png'  # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())


def Header(app):
    return html.Div([get_header(app), html.Br([])])


def get_header(app):
    return html.Div(
        children=[
            html.Div(
                html.H1('Welcome to our awesome dashboard'),
                className='nine columns'
            ),
            html.Div(
                html.Img(
                    src='data:image/png;base64,{}'.format(encoded_image.decode()),
                    style={'height': '40px', 'width': '40px'}
                ),
                className='one columns'
            ),
            html.Div(
                html.A(
                    id="learn_more",
                    children=html.Button("Dash Documents"),
                    href="https://dash.plotly.com",
                ),
                className='two columns'
            ),
        ],
        className='row',
        style={'padding-top': '20px', 'padding-bottom': '20px', 'border-bottom': '2px solid grey',
               'padding-left': '100px', 'padding-right': '100px'}
    )
