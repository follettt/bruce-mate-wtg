# -*- coding: utf-8 -*-
"""
Header
"""
# secrets management for user name
# map pane
# ******** Clear all button?
# Clear main pane unless selections made
# Persist DB connection
# Query definitions and sorting

import streamlit as st 
import pandas as pd 
#import numpy as np 
# import psycopg2 as pg
from datetime import datetime as dt
#import plotly.express as px
import wtg_gui_data_loader as dl

st.set_page_config(page_title="WTG Data Archive", page_icon=None, layout="wide",
                   initial_sidebar_state="expanded", menu_items=None)
# Constants
SEL_DATA = 'C:\\Database\\WTG\\wtg_project_list.csv'
ISO_DATA = 'C:\\Database\\WTG\\test_isotope.csv'
LOC_DATA = 'C:\\Database\\WTG\\encounter.csv'

## ****Put it on each load?
@st.experimental_memo
def load_projects(): #SEL_DATA = 'C:\\Database\\WTG\\wtg_project_list.csv'
    select_data = pd.read_csv(SEL_DATA)
    #select_data = pd.read_csv(dl.PROJECTS)
    return select_data
def load_iso():
    iso_data = pd.read_csv(ISO_DATA)
    return iso_data    
def load_argos():
    #loc_data = pd.read_csv()
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

## Initial df
df_proj = load_projects()

## SIDEBAR -- Select initial projects
with st.sidebar:
    st.title('WTG Telemetry Data Archive')
    st.caption('(Leave any box empty to select ALL)')
    ## Species list
    species_selected = st.multiselect('Species',dl.select_box.species)
    if len(species_selected) > 0:
        df_species = df_proj[(df_proj['species'].isin(species_selected))]
    else:
        df_species = df_proj
    #del df_proj
    ## Year list
    years_selected = st.multiselect('Years',df_species['project_year'].drop_duplicates())
    if len(years_selected) > 0:
        df_years = df_species[(df_species['project_year'].isin(years_selected))]
    else:
        df_years = df_species
    #del df_species
    ## Ocean list
    regions_selected = st.multiselect('Ocean Regions',df_years['ocean_region'].drop_duplicates())
    if len(regions_selected) > 0:
        df_regions = df_years[(df_years['ocean_region'].isin(regions_selected))]
    else:
        df_regions = df_years
    #del df_years
    ## Area list
    areas_selected = st.multiselect('Administrative Regions',df_regions['area'].drop_duplicates())
    if len(areas_selected) > 0:
        df_areas = df_regions[(df_regions['area'].isin(areas_selected))]
    else:
        df_areas = df_regions
    #del df_regions
    ## Project list
    projects_selected = st.multiselect('Projects',df_areas['project'].drop_duplicates())
    
    if len(projects_selected) > 0:
    # For filtering downstream dataframes
        df_projects = df_areas[(df_areas['project'].isin(projects_selected))] #.set_index('project')
    else:
        df_projects = df_areas #.set_index('project')
    #del df_areas        

# Split window in half
col1, col2 = st.columns(2)
## Select choice for next level 
explore = st.radio('Browse:', ['Locations','Animals','Tags'])
if explore == 'Locations':
    # ALSO: filter by Animal first
    # LOAD animal data
    #animals_selected = st.multiselect('Individuals')
    location_sel = col1.multiselect('Location Categories', dl.select_box.loc_types.keys())
    st.caption('Choose one category to see its metadata, choose multiple for geodata only')
    map_btn = col2.button('Show Map')

    if len(location_sel) == 1:
        if location_sel == 'Argos':
            pass
            df_loc = load_argos()
            #df_loc.set_index('feature_id') # trying to omit feature_id from panel
        ## assemble filter from selections
            loc_filter = (df_loc['project_id'].isin(projects_selected)) & \
                      (df_loc['species'].isin(species_selected)) & \
                      (df_loc['feature_type'].isin([dl.select_box.loc_types[k] for k in location_sel]))
            show_data(df_loc[(loc_filter)])
        
        elif location_sel == 'FastLoc':
            pass            
        elif location_sel == 'Deployment':
            pass            
        elif location_sel == 'Biopsy':
            pass            
        elif location_sel ==  'Photo-ID':
            pass        
    elif len(location_sel) > 1:
        loc_filter = (df_loc['project_id'].isin(projects_selected)) & \
                  (df_loc['species'].isin(species_selected)) & \
                  (df_loc['feature_type'].isin([dl.select_box.loc_types[k] for k in location_sel]))
        show_data(df_loc[(loc_filter)])

    ## Build mapping *******************
        if map_btn:
            # display a map in col2
            # call from map_loader
            # maximize button
            #loc_map = px.line_geo()
            pass

# ANIMAL data chosen     
elif explore == 'Animals':
    ## Choose data Category
    category = col1.radio('Choose:', ['Biomarkers', 'Sample Collection', 'Tag Deployments'])
    ## Biomarkers **************************
    if category == 'Biomarkers':
        biomarkers_sel = col1.selectbox('Biomarker Types',  dl.select_box.bio_types)
        if len(biomarkers_sel) > 0: 
            df_iso = load_iso()   
            bio_filter = (df_iso['project_id'].isin(projects_selected)) & \
                          (df_iso['species'].isin(species_selected)) 
            show_data(df_iso[(bio_filter)])
    ## Sample metadata
    elif category == 'Samples Collected':
        pass
    ## Deploy metadata
    elif category == 'Tag Deployments':
        pass

## TAG data chosen
elif explore == 'Tags':
    st.subheader('Tag-derived data')
    category = st.radio('Choose Tag Type:',  dl.select_box.tag_types.keys())
    # show tags with metadata by default
    if category == 'Location Only':    
        pass
    elif category == 'Dive Sumary':
        pass
    elif category == 'Dive Behavior':
        pass




