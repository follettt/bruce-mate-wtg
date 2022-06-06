# -*- coding: utf-8 -*-
"""

@author: follettt
"""
from pandas import read_csv
from streamlit import experimental_memo
## Constants

# USER = '' --->>> Look into Secrets file
BOXDIR = 'C:\\Users\\follettt\\Box\\WHET_LAB\\data\\MMIData Server\\Database'
LOCALDIR = 'C:\Database\WTG'


ISO_DATA = 'C:\\Database\\WTG\\test_isotope.csv'
LOC_DATA = 'C:\\Database\\WTG\\encounter.csv'

## ===>>> Only need one function

def load_projects(): 
    filter_data = read_csv('\\'.join([BOXDIR, 'wtg_project_list.csv']))
    return filter_data

@experimental_memo
def load_data(choice):
    csv_data =  read_csv('\\'.join([BOXDIR, choice]))
    return csv_data    

@experimental_memo
def load_locs(choice):   
    #===>> Add a callback to prevent reloading every time?#===>> Add a timer
    loc_data = read_csv('\\'.join([BOXDIR, choice]))
    return loc_data


# pointers to data sources
class encounter(object):
    encounter = 'encounter.csv'
    enc_argos = 'enc_argos.csv'
    enc_biopsy = 'enc_biopsy.csv'
    enc_deploy = 'enc_deploy.csv'
    enc_fastloc = 'enc_fastloc.csv'
    #enc_photo = ''

class animal_data(object):
    animal_meta = 'proj_animal.csv'
    animal_iso = 'test_isotope.csv'
    ## +++++>>>>>> animal_hormone = ''

class tag_data(object):
    tag_meta = 'tag_data_device.csv'
    tel_beh = 'tag_data_tel_behavior.csv'
    tel_count = 'tag_data_tel_counter.csv'
    tel_stat = 'tag_data_tel_status.csv'
    wc_beh = 'tag_data_wc_behavior.csv'
    wc_stat = 'tag_data_wc_status.csv'
    wc_hist_dep1400 = 'tag_data_wc_histo_count_depth_20_1400m.csv'
    wc_hist_dep400 = 'tag_data_wc_histo_count_depth_25_400m.csv'
    wc_hist_dur20 = 'tag_data_wc_histo_count_duration_03_20min.csv'
    wc_hist_dur60 = 'tag_data_wc_histo_count_duration_15_60min.csv'
    wc_hist_tad1400 = 'tag_data_wc_histo_TAD_20_1400m.csv'
    wc_hist_tad400 = 'tag_data_wc_histo_TAD_25_400m.csv'
    wc_hist_tat26 = 'tag_data_wc_histo_TAT_06_26C.csv'
    wc_hist_tat30 = 'tag_data_wc_histo_TAT_10_30C.csv'
    
# Lists, dicts of filter choices
class select_box(object):
    species = ['Blue',
               'Bowhead',
               'Bryde',
               'Fin',
               'Gray',
               'HybridBF',
               'Humpback',
               'RightN',
               'RightS',
               'Sperm']

    loc_types = {'Argos':'argos', 
                 'FastLoc':'fastloc',
                 'Deployment':'deploy',
                 'Biopsy':'sample'}
##                 'Photo-ID':'photo'}
    
    bio_types = ['Hormones',
                 'Stable Isotopes',
                 'What else?']
    
    tag_types =  {'Location Only':'LO',
                  'Dive Summary':'DS',
                  'Dive Measurement': 'DM', # Dive Duration DD absorbed into DM
                  'Advanced Dive Behavior':'ADB'}
    
    # "For the six hour period, " 
    histo_types = ['Percent of Time in Depth or Temperature bins',
                   'Number of dives in Depth bins',
                   'Number of dives in Duration bins']
    
