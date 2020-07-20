import dash
import dash_cytoscape as cyto
import dash_html_components as html
import json

app = dash.Dash(__name__)

with open('net.json', 'r') as f:
    data = json.load(f)

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-compound',
        layout={
            'name': 'breadthfirst',
            'roots': '[id = "Web"]'
            },
        style={'width': '100%', 'height': '1000px'},
        stylesheet=[
            {
                'selector': 'node',
                'style': {'content': 'data(label)'}
            },
            {
                'selector': '.segment',
                'style': {'width': 5}
            },
            {
                'selector': '.joiner',
                'style': {'line-style': 'dashed'}
            }
        ],
        elements=data
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)