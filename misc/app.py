import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(x=[2, 1, 3], y=['a','b','c'], orientation='h')],
    layout_title_text="Native Plotly rendering in Dash"
)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="graph", figure=fig),
])


if __name__ == "__main__":
    app.run_server(debug=True)
