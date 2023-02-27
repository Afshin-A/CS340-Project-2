import plotly.express as px
import plotly.graph_objs as go
from dash import Dash, dcc, html, Input, Output, dash_table as dt
import dash_leaflet as dl
import pandas as pd
import base64
from CRUD import AnimalShelter

# MongoDB Credentials
username = "aacuser"
password = "password1"
auth_db = "AAC"

# Queries for rescue type and preferred dog breeds
get_all_query = {}
watter_rescue_query = {'age_upon_outcome_in_weeks': {'$gt': 26,'$lt': 156}, 'sex_upon_outcome': 'Intact Female', 'breed': {'$in': ['Labrador Retriever Mix', 'Chesapeake Bay Retriever', 'Newfoundland']}}
mountain_wilderness_query = {'age_upon_outcome_in_weeks': {'$gt': 26,'$lt': 156}, 'sex_upon_outcome': 'Intact Male', 'breed': {'$in': ['German Shepherd', 'Alaskan Malamute', 'Old English Sheepdog', 'Siberian Husky', 'Rottweiler']}}
disaster_person_query = {'age_upon_outcome_in_weeks': {'$gt': 20,'$lt': 300}, 'sex_upon_outcome': 'Intact Male', 'breed': {'$in': ['Doberman Pinscher', 'German Shepherd', 'Golden Retriever', 'Bloodhound', 'Rottweiler']}}

try:
    animals = AnimalShelter(username, password, auth_db)
    df = pd.DataFrame(animals.read(get_all_query))
except():
    # Catch exception if cannot connect to MongoDB
    print("Something went wrong when retrieving data.")


# Could not simply use html.Img() in layout. Credits for this workaround to dayxx369 from https://community.plotly.com/t/adding-local-image/4896/17
image_filename = './GraziosoSalvareLogo.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

# Initializing Dash Application
app = Dash('Web App')
# App layout: how web app looks
app.layout = html.Div([
    html.Img(src=f"data:image/png;base64,{encoded_image.decode()}", style={'display': 'block', 'text-align': 'center', 'margin': 'auto'}),
    html.H1("Project 2 by Afshin E. Ahvazi", style={'text-align': 'center'}),
    html.Br(),
    html.Div("Select Query Category"),
    dcc.Dropdown(
        id="query-dropdown",
        options=[
            {'label': 'Water Rescue', 'value': 'Water'},
            {'label': 'Mountain or Wilderness Rescue', 'value': 'Mountain'},
            {'label': 'Disaster Rescue or Individual Tracking', 'value': 'Disaster'},
            {'label': 'Reset', 'value': 'Reset'}
        ]
    ),
    html.Br(),
    dt.DataTable(
        id="datatable",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        sort_action="native",
        sort_mode="multi",
        filter_action="native",
        # limit the number of rows in each table row
        page_size=15
    ),
    html.Hr(),
    html.H2("Location of Dogs", style={'text-align': 'center'}),
    html.Div(
        id='geo-map'
    ),
    html.Hr(),
    html.H2("Dog Breeds", style={'text-align': 'center'}),
    html.Div(
        # dcc.Graph(id='bar-chart')
    )
])


# This function triggers when dropdown menu changes. Depending on value, we call an appropriate query (as defined earlier) to MongoDB
@app.callback(
    Output(component_id='datatable', component_property='data'),
    Input(component_id='query-dropdown', component_property='value')
)
def update_data(value):
    cursor = {}
    if value == "Water":
        cursor = animals.read(watter_rescue_query)
    elif value == "Mountain":
        cursor = animals.read(mountain_wilderness_query)
    elif value == "Disaster":
        cursor = animals.read(disaster_person_query)
    elif value == "Reset":
        # Do not query for all data everytime user changes to this value. Instead, send the dataframe once created at the start of application
        return df.to_dict('records')
    return pd.DataFrame(list(cursor)).to_dict('records')


# This function triggers when the data table changes, which itself changes when dropdown menu changes.
@app.callback(
    Output(component_id='geo-map', component_property="children"),
    Input(component_id='datatable', component_property="data")
)
def update_map(data):
    if not data:
        # to avoid errors at start up, return an empty list when no data is available
        return []

    # Create a new dataframe
    df = pd.DataFrame.from_dict(data)

    markers = []

    for i in range(len(df)):
        row = df.iloc[i]
        marker = dl.Marker(position=[row['location_lat'], row['location_long']], children=[
            dl.Tooltip(row['animal_id']),
            dl.Popup([
                html.H1(row['name']),
                html.P(row['breed'])
            ])
        ])
        markers.append(marker)

    # Create the map and return it with the markers as children
    return [
        dl.Map(style={'width': '1000px', 'height': '500px'}, center=[30.75, -97.48], zoom=10, children=[
            dl.TileLayer(id="base-layer-id"),
            *markers
        ])
    ]

# Could not figureout the bar or pie charts. Dash would throw constant errors.
# @app.callback(
#     Output(component_id='bar-chart', component_property='figure'),
#     Input(component_id='datatable', component_property='data')
# )
# def update_bar_chart(data):
#     if not data:
#         return


app.run_server(debug=True, port=8051)
