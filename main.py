import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import math
from math import pi
from PIL import Image

# Load the models
fw_model = pickle.load(open('best_fw_model.pkl', 'rb'))
mf_model = pickle.load(open('mf_model.pkl', 'rb'))
df_model = pickle.load(open('df_model.pkl', 'rb'))
gk_model = pickle.load(open('gk_model.pkl', 'rb'))

# Load the data
data = pd.read_csv('updated_football_player_stats.csv')
print(data.head())

# Function to create radar chart
def create_radar_chart(player_data, features):
    categories = features
    N = len(categories)
    
    values = player_data[features].values.flatten().tolist()
    values += values[:1]
    
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    plt.xticks(angles[:-1], categories, color='grey', size=8)
    ax.plot(angles, values)
    ax.fill(angles, values, 'b', alpha=0.1)
    plt.title(player_data['Player'], size=11, color='blue', y=1.1)
    return fig

# Streamlit UI
st.set_page_config(page_title="Football Scouting AI", page_icon=":soccer:", layout="wide")

# Add a header image
header_image = Image.open('Scout.jpg') 
st.image(header_image, use_container_width=True)

st.title("Football Scouting AI")
st.write("""
Welcome to the Football Scouting AI! This tool helps you find the best football players based on your preferences.
You can select the age range, league, and position of players you are interested in, and the AI will provide you with the top players that best suit your needs.
""")

# Get unique leagues from the dataset for the dropdown
leagues = data['Comp'].unique().tolist()

# User Inputs in the sidebar
st.sidebar.header("Scouting Criteria")
age_range = st.sidebar.slider("Select Age Range", min_value=16, max_value=40, value=(20, 25))
league = st.sidebar.selectbox("Select League", leagues)  # Dropdown for leagues
position = st.sidebar.selectbox("Select Position", ["Forward", "Midfielder", "Defender", "Goalkeeper"])

# Filter players based on user inputs
if st.sidebar.button("Scout Players"):
    st.write("Searching for players...")
    
    # Filter data based on position
    if position == "Forward":
        model = fw_model
        position_data = data[data['MainPosition'] == 'FW']
        features = [
            'Goals_per90', 'Shots_per90', 'SoT_per90', 'ShotConversion',
            'SCA_per90', 'GCA_per90', 'PasAss_per90', 'PPA_per90',
            'DribbleSuccess', 'PassAccuracy'
        ]
    elif position == "Midfielder":
        model = mf_model
        position_data = data[data['MainPosition'] == 'MF']
        features = [
            'Assists_per90', 'PasAss_per90', 'PPA_per90', 'SCA_per90',
            'PassAccuracy', 'DribbleSuccess', 'PasProg_per90', 'Press_per90',
            'CarProg_per90', 'Tkl_per90'
        ]
    elif position == "Defender":
        model = df_model
        position_data = data[data['MainPosition'] == 'DF']
        features = [
            'Tkl_per90', 'Int_per90', 'Blocks_per90', 'Clr_per90',
            'TackleSuccess', 'AerialDuelWin%', 'SuccessfulPressure%', 'PassAccuracy',
            'Err_per90'
        ]
    else:
        model = gk_model
        position_data = data[data['MainPosition'] == 'GK']
        features = [
            'Goals_per90', 'SoT_per90', 'PassAccuracy', 'PasTotCmp%',
            'Clr_per90', 'AerialDuelWin%'
        ]
    
    # Filter by age and league
    filtered_players = position_data[
        (position_data['Age'] >= age_range[0]) & 
        (position_data['Age'] <= age_range[1]) & 
        (position_data['Comp'] == league)
    ]
    
    if not filtered_players.empty:
        # Predict and rank players
        filtered_players['Prediction'] = model.predict(filtered_players[features])
        top_players = filtered_players.nlargest(5, 'Prediction')
        
        # Display top players
        st.subheader("Top 5 Players")
        st.dataframe(top_players[['Player', 'Age', 'Comp'] + features])
        
        # Display radar charts for top players
        st.subheader("Player Radar Charts")
        for _, player in top_players.iterrows():
            st.write(f"**{player['Player']}** (Age: {player['Age']}, League: {player['Comp']})")
            fig = create_radar_chart(player, features)
            st.pyplot(fig)
    else:
        st.warning("No players found matching your criteria.")