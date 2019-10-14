from dash import Dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

app = Dash(__name__)

app.layout = html.Div([
    html.H3("Hello, stranger!", id="greeting"),

    html.Br(),
    dcc.Input(id="user_name", placeholder="What's your name?")
])

@app.callback(Output("greeting", "children"),
              [Input("user_name", "value")])
def greet(user_name):
    return f"Hello, {user_name}"

server = app.server

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', debug=True)