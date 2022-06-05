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

@st.experimental_memo
def load_locs():
    loc_data = st.read_csv(dl.LOC_DATA)
    return loc_data

def show_data(in_df):
    hide_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
    st.markdown(hide_index, unsafe_allow_html=True)
    table = st.dataframe(in_df, None, 450) 
    return table


## Initial data for sidebar filters
df_proj = dl.load_projects()
## Still sorted by species!!

with st.sidebar: # -- Select initial project list
    st.title('WTG Telemetry Data Archive')
    st.caption('(Leave box empty to include ALL values)')
    ## Species list
    species_selected = st.multiselect('Species',dl.select_box.species)
#### Trap for a selection ####

## ===>>> Persist Projects even when species changes
    if len(species_selected) > 0:
       ## copy filtered source df to a new df to populate next filter (years)
       # new df      source (            filter on source                )
       df_species = df_proj[(df_proj['species'].isin(species_selected))]
    else: # copy the whole dataframe 
        df_species = df_proj
        
    ## Year list 
    years_selected = st.multiselect('Years',df_species['project_year'].drop_duplicates())
    if len(years_selected) > 0:
        df_years = df_species[(df_species['project_year'].isin(years_selected))]
    else:
        df_years = df_species
   
    ## Ocean list
    regions_selected = st.multiselect('Ocean Regions',df_years['ocean_region'].drop_duplicates())
    if len(regions_selected) > 0:
        df_regions = df_years[(df_years['ocean_region'].isin(regions_selected))]
    else:
        df_regions = df_years
    
    ## Area list
    areas_selected = st.multiselect('Administrative Regions',df_regions['area'].drop_duplicates())
    if len(areas_selected) > 0:
        df_areas = df_regions[(df_regions['area'].isin(areas_selected))]
    else:
        df_areas = df_regions

    ## Project list , ONLY mandatory selector
    projects_selected = st.multiselect('Projects',df_areas['project'].drop_duplicates())
    st.caption('Must select at least one Project to display data')
    if len(projects_selected) > 0:
    # filter subsequent dataframes
        df_projects = df_areas[(df_areas['project'].isin(projects_selected))] #.set_index('project')
    else:
        df_projects = df_areas #.set_index('project')
# Split upper frame
col1, col2, col3, col4 = st.columns(4)

## --------------Select choice for next level---------------------
explore = col1.radio('Browse:', ['Animals','Encounters','Tags'])

## Locations
if explore == 'Encounters':
    df_loc = dl.load_locs()
    location_sel = col2.multiselect('Location Categories', dl.select_box.loc_types.keys())
    col2.caption('Choosing multiple types will display geodata only. \
                 Choose a single type to see all of its metadata.')
    map_btn = col2.button('Show Map')

    if location_sel:
        # ALSO: filter by Animal first     ==>> LOAD animal data
       
        # properly format dates                
        df_loc['timevalue'] = pd.to_datetime(df_loc['timevalue']).dt.strftime('%m-%d-%Y %H:%M:%S')
        #df_loc.set_index('feature_id') # ===>>>Trying to omit feature_id from panel
        #animals_selected = st.multiselect('Individuals')

        if len(location_sel) == 1:
            if location_sel == 'Argos':
                ## assemble filter from selections
    #            loc_filter = (df_loc['project_id'].isin(projects_selected)) & \
    #                      (df_loc['species'].isin(species_selected)) & \
    #                      (df_loc['feature_type'].isin([dl.select_box.loc_types[k] & \
    #                        for k in location_sel]))
    #            show_data(df_loc[(loc_filter)])
                pass
            elif location_sel == 'FastLoc':
                pass            
            elif location_sel == 'Deployment':
                pass            
            elif location_sel == 'Biopsy':
                pass            
            elif location_sel == 'Photo-ID':
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

## >>> what about re-tagged animals? in table for each tag??
elif explore == 'Animals': 
    ## Choose data Category
    category = col2.radio('Choose:', ['Animal Metadata', 'Sample Biomarkers', 'Samples Collected', 'Tags Deployed'])

    if category == 'Animal Metadata': 
        # ===>NEED list of animals from project instead of init_proj
        # csv has "Hump" "Bow" etc.
        df_animal_data = dl.load_animal(dl.animal_data.animal_meta) 
        if species_selected:
            data_filter = (df_animal_data['init_project'].isin(projects_selected)) & \
                          (df_animal_data['species_name'].isin(species_selected))
        else:
            data_filter = (df_animal_data['init_project'].isin(projects_selected)) 
        show_data(df_animal_data[(data_filter)])

    if category == 'Sample Biomarkers':
        biomarkers_sel = col3.selectbox('Biomarker Types',  dl.select_box.bio_types)
        if len(biomarkers_sel) > 0: 
            df_iso = dl.load_iso()   
            bio_filter = (df_iso['project_id'].isin(projects_selected)) & \
                          (df_iso['species'].isin(species_selected)) 
            show_data(df_iso[(bio_filter)])

    elif category == 'Samples Collected':
        pass

    elif category == 'Tags Deployed':
        pass

elif explore == 'Tags':         # show tags with metadata by default
    dtype = col2.radio('Choose: ', ['Tag Metadata','Tag Measurement Data'])
    # display tags from selected projects
    df_devices = dl.load_meas(dl.tag_data.tag_meta) 
    dev_filter = (df_devices['project_id'].isin(projects_selected)) & \
                 (df_devices['species_name'].isin(species_selected))
    slot1 = st.empty()
    with slot1.container():
        show_data(df_devices[(dev_filter)])
    if dtype == 'Tag Metadata': 
        # another selectbox for addl sched and hware
        pass
      
    elif dtype == 'Tag Measurement Data':
        # hide device list
        slot1.empty()
        tagtype = col3.radio('Choose Tag Type:',  dl.select_box.tag_types.keys())
    ## DiveSum tags
        if tagtype == 'Dive Summary':
            col3.caption('Wildlife Computers SPOT Tags') 
            tag_list = df_devices['tag_name'][(df_devices['tag_class'] == 'DiveSum') & \
                                (df_devices['project_id'].isin(projects_selected))]  
        ## Report type
            report = col4.radio('Report:', ['Behavior Histogram', 'Tag Status'])
            if report == 'Behavior Histogram':
                if 'Sperm' in species_selected:
                     df_tag_data = dl.load_meas(dl.tag_data.wc_hist_tat30) 
                else:
                     df_tag_data = dl.load_meas(dl.tag_data.wc_hist_tat26) 
            elif report == 'Tag Status':
                df_tag_data = dl.load_meas(dl.tag_data.wc_stat)
            data_filter = (df_tag_data['tag_name'].isin(tag_list))  #(df_tag_data['project_id'].isin(projects_selected))  
            with slot1.container():
                show_data(df_tag_data[(data_filter)])
                #table = st.dataframe(tag_list, None, 450) 
 ## DiveMon
        elif tagtype == 'Dive Measurement': #RDW640-665
            col3.caption('Telonics RDW640/665 Tags') 
            tag_list = df_devices['tag_name'][(df_devices['tag_class'] == 'DiveMon') & \
                                (df_devices['project_id'].isin(projects_selected))]  
         ## Report type
            report = col4.radio('Report:', ['Dive Behavior', 'Tag Status'])
            if report == 'Dive Behavior':
                df_tag_data = dl.load_meas(dl.tag_data.tel_beh) 
            elif report == 'Tag Status':
                df_tag_data = dl.load_meas(dl.tag_data.tel_stat)
            data_filter = (df_tag_data['tag_name'].isin(tag_list)) 
            with slot1.container():
                show_data(df_tag_data[(data_filter)])
            
  ## ADB
        elif tagtype == 'Advanced Dive Behavior':
            col3.caption('Wildlife Computers MK-10 PAT Tags') 
            tag_list = df_devices['tag_name'][(df_devices['tag_class'] == 'ADB') & \
                                (df_devices['project_id'].isin(projects_selected))] 
         ## Report type
            report = col4.radio('Report:', ['Behavior Histogram','Dive Behavior', 'Tag Status'])
            if report == 'Behavior Histogram':                
                ## choose report TAT/D, DDEP, DDUR OR  
                histo_type = col4.radio('Choose one:', dl.select_box.histo_types)
                if 'Sperm' in species_selected:
                    if histo_type == dl.select_box.histo_types[0]: # TAT/TAD
                        df_tag_data = dl.load_meas(dl.tag_data.wc_hist_tad1400) 
                    elif histo_type == dl.select_box.histo_types[1]: # DDEP
                        df_tag_data = dl.load_meas(dl.tag_data.wc_hist_dep1400)
                    elif histo_type == dl.select_box.histo_types[2]: # DDUR
                        df_tag_data = dl.load_meas(dl.tag_data.wc_hist_dur60)   
                else:
                    if histo_type == dl.select_box.histo_types[0]: # TAT/TAD
                        df_tag_data = dl.load_meas(dl.tag_data.wc_hist_tad400) 
                    elif histo_type == dl.select_box.histo_types[1]: # DDEP
                        df_tag_data = dl.load_meas(dl.tag_data.wc_hist_dep400)
                    elif histo_type == dl.select_box.histo_types[2]: # DDUR
                        df_tag_data = dl.load_meas(dl.tag_data.wc_hist_dur20)                      
            elif report == 'Dive Behavior':
                df_tag_data = dl.load_meas(dl.tag_data.wc_beh) 
            elif report == 'Tag Status':
                df_tag_data = dl.load_meas(dl.tag_data.wc_stat)    
            
            data_filter = (df_tag_data['tag_name'].isin(tag_list)) 
            with slot1.container():
                show_data(df_tag_data[(data_filter)])            
 ## Location
        elif tagtype == 'Location Only': 
            col3.caption('Telonics "ST" class Tags') 
            df_tag_data = dl.load_meas(dl.tag_data.tel_count) 
            data_filter = (df_tag_data['project_id'].isin(projects_selected))
            st.caption(' Parameters = CNOS: Cumulative Number Of Surfacings, \
                        CNOT: Cumulative Number Of Transmissions or  \
                        CTAS: Cumulative Time At Surface (seconds)')
            show_data(df_tag_data[(data_filter)])


