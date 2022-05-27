# -*- coding: utf-8 -*-
"""
Header
"""
import streamlit as st 
import pandas as pd 
#import numpy as np 
# import psycopg2 as pg
from datetime import datetime as dt
import plotly.express as px

st.set_page_config(page_title="WTG Data Archive", page_icon=None, layout="wide",
                   initial_sidebar_state="expanded", menu_items=None)

SEL_DATA = 'C:\\Database\\WTG\\wtg_project_list.csv'
ISO_DATA = 'C:\\Database\\WTG\\test_isotope.csv'
LOC_DATA = 'C:\\Database\\WTG\\encounter.csv'
BOX_DIR = 'C:\\Users\\follettt\\Box\\WHET_LAB\\data\\MMIData Server\\Database'
# secrets management for user name
# map pane



#  PERSIST SELECTIONS?
# ******** Clear all button
# Clear main pane unless selections made
# Persist DB connection
# Query definitions and sorting


def load_selectors():
    select_data = pd.read_csv(SEL_DATA)
    return select_data

def load_iso():
    iso_data = pd.read_csv(ISO_DATA)
    return iso_data    

@st.experimental_memo
def load_argos():
    loc_data = pd.read_csv(LOC_DATA)
    loc_data['timevalue'] = pd.to_datetime(loc_data['timevalue']).dt.strftime('%m-%d-%Y %H:%M:%S')
    return loc_data

def show_data(in_df):
    hide_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
    st.markdown(hide_index, unsafe_allow_html=True)
    st.dataframe(in_df) 

## SIDEBAR -- Select initial projects
df_sel = load_selectors()
with st.sidebar:
    st.title('WTG Telemetry Data Archive')
    st.caption('(Leave any box empty to select ALL)')
## Species
    species_selected = st.multiselect('Species',df_sel['species'].drop_duplicates())
    if len(species_selected) > 0:
        df_species = df_sel[(df_sel['species'].isin(species_selected))]
    else:
        df_species = df_sel
## Years
    years_selected = st.multiselect('Years',df_species['project_year'].drop_duplicates())
    if len(years_selected) > 0:
        df_years = df_species[(df_species['project_year'].isin(years_selected))]
    else:
        df_years = df_species
## Oceans
    regions_selected = st.multiselect('Ocean Regions',df_years['ocean_region'].drop_duplicates())
    if len(regions_selected) > 0:
        df_regions = df_years[(df_years['ocean_region'].isin(regions_selected))]
    else:
        df_regions = df_years
## Areas
    areas_selected = st.multiselect('Administrative Regions',df_regions['area'].drop_duplicates())
    if len(areas_selected) > 0:
        df_areas = df_regions[(df_regions['area'].isin(areas_selected))]
    else:
        df_areas = df_regions
## Projects
    projects_selected = st.multiselect('Projects',df_areas['project'].drop_duplicates())
    if len(projects_selected) > 0:
        df_projects = df_areas[(df_areas['project'].isin(projects_selected))] #.set_index('project')
    else:
        df_projects = df_areas #.set_index('project')
## Finally:
    explore = st.radio('Browse:', ['Tag Data', 'Animal Data'])

## SelectBox Dicts / Lists
loc_types = {'Argos':'argos', 
             'FastLoc':'fastloc',
             'Deployment':'deploy',
             'Biopsy':'biopsy',
             'Photo-ID':'photo'}
bio_types = ['Hormones','Stable Isotopes','What else?']
tag_types =  {'Location Only':'LO',
              'Dive Summary':'DS',
              'Dive Measurement': 'DM',
              'Adv. Dive Behavior':'ADB'}

# Refine Selections    
if explore == 'Animal Data':
    st.subheader('Animal & Geodata')
    category = st.radio('Choose:', ['Locations', 'Biomarkers'])
    col1, col2 = st.columns(2)
    if category == 'Locations':
        location_sel = col1.multiselect('Location Categories', loc_types.keys())
        map_btn = col2.button('Show Map')
        # **** IF multiple types, show encounter rows only, otherwise all rows
        if len(location_sel) > 0: 
            df_loc = load_argos()
#            df_loc.set_index('feature_id')
            # construct Argos filter
            loc_filter = (df_loc['project_id'].isin(projects_selected)) & \
                          (df_loc['species'].isin(species_selected)) & \
                          (df_loc['feature_type'].isin([loc_types[k] for k in location_sel]))
            show_data(df_loc[(loc_filter)])

    else:
        biomarkers_sel = col1.selectbox('Biomarker Types', bio_types)
        if len(biomarkers_sel) > 0: 
            df_iso = load_iso()   
            bio_filter = (df_iso['project_id'].isin(projects_selected)) & \
                          (df_iso['species'].isin(species_selected)) 
#                          (df_iso['species'].isin(species_selected))    
            show_data(df_iso[(bio_filter)])
        
elif explore == 'Tag Data':
    st.subheader('Tag-derived data')
    category = st.radio('Choose Tag Type:', tag_types.keys())
    # show tags with metadata by default
    if category == 'Location Only':    
        pass
    elif category == 'Dive Sumary':
        pass
    elif category == 'Dive Behavior':
        pass
        
        
    
