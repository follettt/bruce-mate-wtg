# -*- coding: utf-8 -*-
"""
Header
"""
# =============================================================================
# Canyouget2that?

# secrets management for user name
# Clear main pane unless selections made
# Query definitions and sorting
# >>ASSERT<< radio lists if data exists for selections
# =============================================================================
## Streamlit FYI: every widget interaction causes a rerun of the app

import streamlit as st 
#import pandas as pd 
#from datetime import datetime as dt
#import plotly.express as px
import geopandas as gpd
#from shapely.geometry import Point, LineString, shape
###  import matplotlib.pyplot

import wtg_gui_data_loader as dl
# import wtg_gui_functions as wgf
# import wtg_gui_sources as wgs
# import wtg_gui_contstants as wgc

## NEW COLORS 
st.set_page_config(page_title="Whale Telemetry Data Archive Online System", page_icon=None, layout="wide",
                   initial_sidebar_state="expanded", menu_items=None)

def show_data(in_df):
  ## inject CSS to hide index
    hide_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
    st.markdown(hide_index, unsafe_allow_html=True)
  ## display the csv
    table = st.dataframe(in_df, None, 450) 
    return table

#### MOVE to functions
@st.experimental_memo
def export_csv(df):
    return df.to_csv().encode('utf-8')

# =============================================================================
# def selector(params):
#   box = st.multiselect(params[0], params[1])
#   return box
# =============================================================================

## Initial csv data for sidebar filters
df_proj = dl.load_projects()

with st.sidebar:
#    usr = st.text_input('Enter username for Box access: ')
##    st.subheader('Bruce & MaryLou Mate')
    st.subheader('Whale Telemetry Data Archive Online System')
#### TRAP here if user not entered
    # if not usr:
    # not using slots yet 
    # slot1 = st.empty()    
## Start with Species list
    st.caption('(Leave any box empty to include ALL values)')
    st.caption('')
#=============================================================================
## {widget name: (Title, default content}
#     w_names = ['species_selected',
#                'years_selected',
#                'regions_selected',
#                'areas_selected',
#                'projects_selected']

#     w_dict = {'species_selected':('Species', dl.select_box.species), 
#                 'years_selected':('Years', df_proj["project_year"].drop_duplicates()),
#                 'regions_selected':('Ocean Regions', df_proj["ocean_region"].drop_duplicates()),
#                 'areas_selected':('Administrative Regions', df_proj["area"].drop_duplicates()),
#                 'projects_selected':('Projects', df_proj["project"].drop_duplicates())}
#     def_dict = {}
# # default values lists
#     spp_def = dl.select_box.species
#     year_def = df_proj["project_year"].drop_duplicates()
#     region_def = df_proj["ocean_region"].drop_duplicates()
#     area_def = df_proj["area"].drop_duplicates()
#     project_def = df_proj["project"].drop_duplicates()
# # create selectboxes from default values?
#     species_selected = st.multiselect('Species', spp_def)
#     years_selected = st.multiselect('Years', year_def)
#     regions_selected = st.multiselect('Ocean Regions', )
#     areas_selected = st.multiselect('Administrative Regions', region_def)
#     projects_selected = st.multiselect('Projects', project_def)

## look for changes to widgets using dict
    # local_vars = locals()
    # for wn in w_names:
    #   local_vars = locals()
    #   local_vars.__setitem__(wn, w_dict.something)
    #   if local_vars[-1] != 'dict of default lists'
   
     
    # species_filter = (df_proj["species"].isin(species_selected))     # this is a df or not?
         
    # years_selected = st.multiselect('Years', df_proj["project_year"].loc[(species_filter)].drop_duplicates())
         

         
    ## Get year list from filtered species 
         # years_selected = st.multiselect('Years',df_species['project_year'].drop_duplicates())
         # if len(years_selected) > 0:
         #     df_years = df_species[(df_species['project_year'].isin(years_selected))]
         # else:
         #     df_years = df_species
             
# =============================================================================

#     species_selected = st.multiselect('Species',spp_list) 
#     with slot1.container():
#         years_selected = st.multiselect('Years', df_proj["project_year"].drop_duplicates())
#         regions_selected = st.multiselect('Ocean Regions', df_proj["ocean_region"].drop_duplicates())
#         areas_selected = st.multiselect('Administrative Regions', df_proj["area"].drop_duplicates())
#         projects_selected = st.multiselect('Projects', df_proj["project"].drop_duplicates()) 
## MS name: default content
#   MS_dict = {years_selected:('Years', df_proj["project_year"].drop_duplicates()),
#            regions_selected:('Ocean Regions',df_proj["ocean_region"].drop_duplicates()),
#            areas_selected:('Administrative Regions',df_proj["area"].drop_duplicates()),
#            projects_selected:('Projects',df_proj["project"].drop_duplicates())}


# =============================================================================
#     if species_selected: # save and propogate to other selectors   Else: keep current selectors
# 
#         species_filter = (df_proj["species"].isin(species_selected))    
#         years_selected = st.multiselect('Years', df_proj["project_year"].loc[(species_filter)].drop_duplicates())
#         regions_selected = st.multiselect('Ocean Regions', df_proj["ocean_region"].loc[(species_filter)].drop_duplicates() )
#         areas_selected = st.multiselect('Administrative Regions',df_proj["area"].loc[(species_filter)].drop_duplicates())
#         projects_selected = st.multiselect('Projects',df_proj["project"].loc[(species_filter)].drop_duplicates()) 
#    
#     else:
#             if years_selected:
#                
#                year_filter = (df_proj["project_year"].isin(years_selected))
#                regions_selected = st.multiselect('Ocean Regions', \
#                                 df_proj["ocean_region"].loc[ \
#                                 (species_filter)].drop_duplicates())
#               
#                areas_selected = st.multiselect('Administrative Regions', \
#                                     df_proj["area"].loc[ \
#                                     (species_filter)].drop_duplicates())
#                projects_selected = st.multiselect('Projects', \
#                                     df_proj["project"].loc[ \
#                                     (species_filter)].drop_duplicates()) 
# 
#         years =    df_proj["project_year"].loc[(species_filter)].drop_duplicates()
#         regions =  df_proj["ocean_region"].loc[(species_filter)].drop_duplicates() 
#         areas =    df_proj["area"].loc[(species_filter)].drop_duplicates()
#         projects = df_proj["project"].loc[(species_filter)].drop_duplicates()
# # load multiselects
# #    projects_selected, areas_selected, regions_selected, years_selected = \
# #            show_multi(projects, areas, regions, years)    
#     years_selected = st.multiselect('Years', years)
#     if years_selected:
#         year_filter = (df_proj["project_year"].isin(years_selected))
#         reg_sel1 = st.multiselect('Ocean Regions',regions)
#     if regions_selected:
#         region_filter = (df_proj["ocean_region"].isin(regions_selected)) 
#     areas_selected = st.multiselect('Administrative Regions',areas)
#     if areas_selected:
#         project_filter = (df_proj["area"].isin(areas_selected)) 
#     projects_selected = st.multiselect('Projects',projects) 
 
#         Got lots of ‘elifs’ for your if statement? Use a dictionary!
# =============================================================================
 ## Default all species
    species_selected = st.multiselect('Species',dl.select_box.species) 
## SAVE this side bar***************************************************************************
    if species_selected:
##unused        species = df_proj['species'].drop_duplicates()
        # df_species = df_proj[(df_proj['species'].isin(species_selected))]
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
    ## Finally Project list; ONLY mandatory selector
##    st.caption('Select at least one Project to display data')
    ## Projects
    projects_selected = st.multiselect('Projects',df_areas['project'].drop_duplicates())
    if len(projects_selected) > 0:
    # filter subsequent dataframes
        df_projects = df_areas[(df_areas['project'].isin(projects_selected))] #.set_index('project')
    else:
        df_projects = df_areas #.set_index('project')
##end save *******************************************************************************************************

## Split upper frame into columns
col1, col2, col3, col4 = st.columns(4)

## --------------Select choice for next level---------------------
explore = col1.radio('Choose a category:', ['Animals', 'Encounters', 'Tags'])

# =============================================================================
# #### LOCATIONS ###### loc_types
# =============================================================================
if explore == 'Encounters':
  ## Load full animal list 
    df_animals = dl.load_data(dl.animal_data.animal_meta).set_index('animal_id')
  ## Primary proj/species filter 
    spp_filt = (df_animals['species'].isin(species_selected))
    prj_filt = (df_animals['project_id'].isin(projects_selected))
    if projects_selected and species_selected:
        anim_list = (df_animals['animal_name'][(prj_filt) & (spp_filt)])
    elif projects_selected:
        anim_list = (df_animals['animal_name'][(prj_filt)])
    elif species_selected: 
        anim_list = (df_animals['animal_name'][(spp_filt)])
    else:    
        anim_list = df_animals['animal_name']            

  ## Top controls
    anim_select = col2.multiselect('Select animals (optional)', anim_list)    

    location_sel = col3.multiselect('Select Location Type(s):', dl.select_box.loc_types.keys())
    col3.caption('Select one to show metadata for that type; Select multiple to show geodata only')
    
    display = col4.radio('Choose display:',['Show Table', 'Show Map'])
  ## Wait for enc-type selection
    if location_sel:
  ## Make df_loc from specific enc-type metadata
        if len(location_sel) == 1:
            if location_sel[0] == 'Argos':
                df_loc = dl.load_locs(dl.encounter.enc_argos).set_index('feature_id')
                
#### NOT working ???? ################################                
               # df_loc[(df_loc['hide'] == 'FALSE')]
#####################################################    
            
            elif location_sel[0] == 'FastLoc':
                df_loc = dl.load_locs(dl.encounter.enc_fastloc).set_index('feature_id')
            elif location_sel[0] == 'Deployment':
                df_loc = dl.load_locs(dl.encounter.enc_deploy).set_index('feature_id')
            elif location_sel[0] == 'Biopsy':
                df_loc = dl.load_locs(dl.encounter.enc_biopsy).set_index('feature_id')   

    ## Primary filter ---> apply to df_loc at switcher 
            if anim_select:
                loc_filter = (df_loc['animal_name'].isin(anim_select))
            else:
                loc_filter = (df_loc['animal_name'].isin(anim_list))

  ## Make df_loc from selected enc-types
        elif len(location_sel) > 1:  
        ## 1- Load encounter (xy points) csv
            df_loc = dl.load_locs(dl.encounter.encounter).set_index('feature_id')

    ## Secondary filter --- animals, feature-type
            if anim_select: 
                loc_filter = (df_loc['animal_name'].isin(anim_select)) & \
                             (df_loc['feature_type'].isin( \
                                    [dl.select_box.loc_types[k] for k in location_sel])) & \
                                 (df_loc['hide'] == 'FALSE')
            else:
                loc_filter = (df_loc['animal_name'].isin(anim_list)) & \
                             (df_loc['feature_type'].isin([dl.select_box.loc_types[k] \
                                                           for k in location_sel])) & \
                             (df_loc['hide'] == 'FALSE')
### End IF location_sel

  ## Display switcher
        slot2 = st.empty()
        with slot2.container():
            if display == 'Show Table':
    ## Apply filters 
    ## Display dataframe
                show_data(df_loc[(loc_filter)])
                col1, col2, col3, col4 = st.columns(4)
                
            ## Table controls
                # Select export type 
                # export = col1.radio('Download as: ', ['CSV','Excel'])#,'Shapefile'])        
                # if export == 'CSV':
                out_file = export_csv(df_loc[(loc_filter)])
                col1.download_button('Download CSV', out_file, 'export_encounters.csv', 'text/csv')  
                #elif export == 'Excel':
                #    pass


### Display Map   
            elif display == 'Show Map':
                loc_filter = loc_filter & (df_loc['latitude'].notna()) 
                df = df_loc[(loc_filter)]
                #st.map(df) # Basic Streamlit map -->> can only display Points
            ## geopandas points
                pts = gpd.points_from_xy(df.longitude, df.latitude)
                gdf = gpd.GeoDataFrame(df, geometry=pts, crs='EPSG:4326')
                st.map(gdf)

# =============================================================================
# 
#     ## OR pyplot map
# 
#         # Screen for >1 location to make either points or lines
#          ## Lines from geopandas + shapely 
# #                df_LS = gdf.groupby(['tag_name'])['geometry'].apply(lambda x: LineString(x.tolist())) 
#          ## ERROR:  LineStrings must have at least 2 coordinate tuples
# 
# ### next step, display that mf
# ## >>> Map should be 180 center
#                  
#                ## geopandas snips
#                 # pts = gpd.points_from_xy(df.longitude, df.latitude)
#                 # gdf = gpd.GeoDataFrame(df, geometry=pts, crs='EPSG:4326')
#                 # linestr = gdf.groupby(['tag_name'])['geometry'].apply(lambda x: LineString(x.tolist()))
#                 # New df from linestr  
#                 #lines = gpd.GeoDataFrame(linestr, geometry='geometry', crs="EPSG:4326") 
#                 # lines.reset_index(inplace=True)
#                 # lines.plot()#column='tag_id')
#             
#                 ## from 
# #                 world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# #                 # ax: matplotlib axes instance - matplotlib.pyplot.Artist (default None)
# #                 ax = world[world.continent == 'North America'].plot(color='white', edgecolor='black')
# #                 plt = gdf.plot(ax=ax, color='red')
# #                 plt.show()
#                    # 'AxesSubplot' object has no attribute 'show' 
# =============================================================================


# =============================================================================
# #### ANIMALS ####
# =============================================================================
elif explore == 'Animals': 
    ## WORKING ## ------------------------------------------------------------    
    df_animals = dl.load_data(dl.animal_data.animal_meta).set_index('animal_id')
    ## Choose data Category
    category = col2.radio('Choose a dataset:', ['Animal Metadata', 'Sample Biomarkers'])
    if category == 'Animal Metadata':
        spp_filt = (df_animals['species'].isin(species_selected))
        prj_filt = (df_animals['project_id'].isin(projects_selected))
        if projects_selected and species_selected:
            show_data(df_animals[(prj_filt) & (spp_filt)])
            out_file = export_csv(df_animals[(prj_filt) & (spp_filt)])
        elif projects_selected:
            show_data(df_animals[(prj_filt)])
            out_file = export_csv(df_animals[(prj_filt)])
        elif species_selected: 
            show_data(df_animals[(spp_filt)])
            out_file = export_csv(df_animals[(spp_filt)])
        else:    
            show_data(df_animals)              
            out_file = export_csv(df_animals)
        st.download_button('Download CSV', out_file, 'export_animal_metadata.csv', 'text/csv') 
    
    if category == 'Sample Biomarkers':
# =============================================================================
# #         ### confirm project exists in each file first
#         biofiles = [(dl.animal_data.animal_isotope),
#                     (dl.animal_data.animal_hormone),
#                     (dl.animal_data.animal_genes)]
#         if projects_selected:
#             in_bio = []
#             for biof in biofiles:
#                 if dl.load_data(biof).isin(projects_selected)['project_id'].any():
#                     in_bio.append(biofiles.index(biof))
#             if in_bio: # any hits?
#                 
#     biomarkers_sel = col3.radio('Select Biomarker types', dl.select_box.bio_types)
# 
# =============================================================================
    ## WORKING ## ------------------------------------------------------------     
        biomarkers_sel = col3.radio('Choose a biomarker type', dl.select_box.bio_types)
        if biomarkers_sel == dl.select_box.bio_types[2]:
            df_bio = dl.load_data(dl.animal_data.animal_genes) 
        if biomarkers_sel == dl.select_box.bio_types[1]:
            df_bio = dl.load_data(dl.animal_data.animal_hormone) 
        if biomarkers_sel == dl.select_box.bio_types[0]:    
            df_bio = dl.load_data(dl.animal_data.animal_isotope) 
        spp_filt = (df_bio['species'].isin(species_selected))
        prj_filt = (df_bio['project_id'].isin(projects_selected))
        if projects_selected and species_selected:
            show_data(df_bio[(prj_filt) & (spp_filt)])
            out_file = export_csv(df_bio[(prj_filt) & (spp_filt)])
        elif projects_selected:
            show_data(df_bio[(prj_filt)])
            out_file = export_csv(df_bio[(prj_filt)])
        elif species_selected:
            show_data(df_bio[(spp_filt)])
            out_file = export_csv(df_bio[(spp_filt)])
        else:
            show_data(df_bio)
            out_file = export_csv(df_bio)
        st.download_button('Download CSV', out_file, 'export_biomarkers.csv', 'text/csv') 
    ## ------------------------------------------------------------------------


#### TAGS #######
elif explore == 'Tags':         # show tags with metadata by default
    slot1 = st.empty()
    df_devices = dl.load_data(dl.tag_data.tag_meta) 
## Choose data Category
    datatype = col2.radio('Select one: ', ['Basic Metadata','Extended Metadata','Measured Data'])

    if datatype == 'Basic Metadata': 
        tagtype = col3.multiselect('Select Tag Type(s):',dl.select_box.tag_types.keys()) 
        spp_filter = (df_devices['species_name'].isin(species_selected))
        prj_filter = (df_devices['project_id'].isin(projects_selected))

        with slot1.container():
            tag_filter = (df_devices['tag_type'].isin( \
                            dl.select_box.tag_types.values())) 
            if tagtype:
                tag_filter = (df_devices['tag_type'].isin( \
                                 dl.select_box.tag_types[k] for k in tagtype))
                
            if species_selected and projects_selected:
                show_data(df_devices[(tag_filter) & \
                                     (prj_filter) & \
                                     (spp_filter)])
                out_file = export_csv(df_devices[(tag_filter) & \
                                     (prj_filter) & \
                                     (spp_filter)])
            elif projects_selected: 
                show_data(df_devices[(tag_filter) & (prj_filter)]) 
                out_file = export_csv(df_devices[(tag_filter) & (prj_filter)])
            elif species_selected:
                show_data(df_devices[(tag_filter) & (spp_filter)]) 
                out_file = export_csv(df_devices[(tag_filter) & (spp_filter)])
            else:    
                show_data(df_devices[(tag_filter)])
                out_file = export_csv(df_devices[(tag_filter)])
        
        st.download_button('Download CSV', out_file, 'export_tag_metadata.csv', 'text/csv') 
### ADD @@@ another selectbox for addl sched and hware

 ## Measurements          
    elif datatype == 'Measured Data':
       # hide devices list
       slot1.empty()
       tagtype = col3.radio('Select one tag type:',dl.select_box.tag_types.keys())
       #tag_list = df_devices['tag_name']
        # Filters for tag_list
       prj_filter = (df_devices['project_id'].isin(projects_selected))
       spp_filter = (df_devices['species_name'].isin(species_selected))
       
    ## DiveSum 
       if tagtype == 'Dive Summary':
            type_filter = (df_devices['tag_class'] == 'DiveSum')
            col3.caption('Wildlife Computers SPOT Tags') 
            if projects_selected and species_selected:
                tag_list = df_devices['tag_name'][(type_filter) & \
                                                  (prj_filter) & \
                                                  (spp_filter)]
            elif projects_selected:
                tag_list = df_devices['tag_name'][(type_filter) & \
                                                  (prj_filter)]
            elif species_selected:
                tag_list = df_devices['tag_name'][(type_filter) & \
                                                  (spp_filter)] 
            else:
                tag_list = df_devices['tag_name'][(type_filter)] 

        ## Report types
            report = col4.radio('Select one report type:', ['Behavior Histogram', 'Tag Utility'])
            if report == 'Behavior Histogram':
                 if 'Sperm' in species_selected:
                      df_tag_data = dl.load_data(dl.tag_data.wc_hist_tat30) 
                 else:
                      df_tag_data = dl.load_data(dl.tag_data.wc_hist_tat26) 
            elif report == 'Tag Utility':
                 df_tag_data = dl.load_data(dl.tag_data.wc_stat)
             
            data_filter = (df_tag_data['tag_name'].isin(tag_list)) 
            with slot1.container():
                 show_data(df_tag_data[(data_filter)])
                 out_file = export_csv(df_tag_data[(data_filter)])
            
            st.download_button('Download CSV', out_file, 'export_wildlife_report.csv', 'text/csv')

    ## DiveMon
       elif tagtype == 'Dive Monitoring': #RDW640-665
            type_filter = (df_devices['tag_class'] == 'DiveMon')
            col3.caption('Telonics RDW640/665 Tags') 
        # Filters for tag_list
            if projects_selected and species_selected:
                tag_list = df_devices['tag_name'][(type_filter) & \
                                                  (prj_filter) & \
                                                  (spp_filter)]
            elif projects_selected:
                tag_list = df_devices['tag_name'][(type_filter) & \
                                                  (prj_filter)]
            elif species_selected:
                tag_list = df_devices['tag_name'][(type_filter) & \
                                                  (spp_filter)] 
            else:
                tag_list = df_devices['tag_name'][(type_filter)] 
        ## Report types
            report = col4.radio('Choose Report type:', ['Dive Behavior', 'Tag Utility'])
            if report == 'Dive Behavior':
                df_tag_data = dl.load_data(dl.tag_data.tel_beh) 
            elif report == 'Tag Utility':
                df_tag_data = dl.load_data(dl.tag_data.tel_stat)

            data_filter = (df_tag_data['tag_name'].isin(tag_list))
            with slot1.container():
                show_data(df_tag_data[(data_filter)])
                out_file = export_csv(df_tag_data[(data_filter)])
            st.download_button('Download CSV', out_file, 'export_telonics_report.csv', 'text/csv')
            
    ## ADB
       elif tagtype == 'Advanced Dive Behavior':
            type_filter = (df_devices['tag_class'] == 'ADB')
            col3.caption('Wildlife Computers MK-10 PAT Tags (Not recovered)') 
            
        # Filters for tag_list
            if projects_selected and species_selected:
                tag_list = df_devices['tag_name'][(type_filter) & \
                                                  (prj_filter) & \
                                                  (spp_filter)]
            elif projects_selected:
                tag_list = df_devices['tag_name'][(type_filter) & \
                                                  (prj_filter)]
            elif species_selected:
                tag_list = df_devices['tag_name'][(type_filter) & \
                                                  (spp_filter)] 
            else:
                tag_list = df_devices['tag_name'][(type_filter)] 
                
        ## Report types
            report = col4.radio('Choose Report type:', ['Behavior Histogram', 
                                                        'Dive Shape', 
                                                        'Tag Utility'])
            if report == 'Behavior Histogram':                
              ## choose report TAT/D, DDEP, DDUR  
                histo_type = col4.radio('Choose histogram type:', dl.select_box.histo_types)
              ## "Deep" tags
                if projects_selected == ['2011GoM']:
                    if histo_type == dl.select_box.histo_types[0]: # TAT/TAD
                        df_tag_data = dl.load_data(dl.tag_data.wc_hist_tad1400) 
                    elif histo_type == dl.select_box.histo_types[1]: # DDEP
                        df_tag_data = dl.load_data(dl.tag_data.wc_hist_dep1400)
                    elif histo_type == dl.select_box.histo_types[2]: # DDUR
                        df_tag_data = dl.load_data(dl.tag_data.wc_hist_dur60)   
              ## "Shallow"
                else: 
                    if histo_type == dl.select_box.histo_types[0]: # TAT/TAD
                        df_tag_data = dl.load_data(dl.tag_data.wc_hist_tad400) 
                    elif histo_type == dl.select_box.histo_types[1]: # DDEP
                        df_tag_data = dl.load_data(dl.tag_data.wc_hist_dep400)
                    elif histo_type == dl.select_box.histo_types[2]: # DDUR
                        df_tag_data = dl.load_data(dl.tag_data.wc_hist_dur20)                      

            elif report == 'Dive Shape':
                df_tag_data = dl.load_data(dl.tag_data.wc_beh) 
    
            elif report == 'Tag Utility':
                df_tag_data = dl.load_data(dl.tag_data.wc_stat)    

            data_filter = (df_tag_data['tag_name'].isin(tag_list)) 
            with slot1.container():
                show_data(df_tag_data[(data_filter)])            
                out_file = export_csv(df_tag_data[(data_filter)])
            st.download_button('Download CSV', out_file, 'export_wildlife_histo.csv', 'text/csv')
    
    ## Location only LO
       elif tagtype == 'Location Only':
            type_filter = (df_devices['tag_class'] == 'Location')
            col3.caption('Telonics "ST" class Tags')
            df_tag_data = dl.load_data(dl.tag_data.tel_count) 
            st.caption(' Parameters = CNOS: Cumulative Number Of Surfacings, \
                        CNOT: Cumulative Number Of Transmissions or  \
                        CTAS: Cumulative Time At Surface (seconds)')
        # Filters for tag_list
            if projects_selected and species_selected:
                tag_list = df_devices['tag_name'][(type_filter) & \
                                                  (prj_filter) & \
                                                  (spp_filter)]
            elif projects_selected:
                tag_list = df_devices['tag_name'][(type_filter) & \
                                                  (prj_filter)]
            elif species_selected:
                tag_list = df_devices['tag_name'][(type_filter) & \
                                                  (spp_filter)] 
            else:
                tag_list = df_devices['tag_name'][(type_filter)] 

            data_filter = (df_tag_data['tag_name'].isin(tag_list)) 
            with slot1.container():
                show_data(df_tag_data[(data_filter)])
                out_file = export_csv(df_tag_data[(data_filter)])
            st.download_button('Download CSV', out_file, 'export_telonics_counter.csv', 'text/csv')

else:
    pass
#### END
