import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide") 

st.title("Interactive Map")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)
    url = st.text_input("Enter custom URL:")

with col1:

    m = leafmap.Map(locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
    if url:
        m.add_tile_layer(url, name="Custom Basemap", attribution="  ")
    else:
        m.add_basemap(basemap)
        
    m.to_streamlit(height=700)
