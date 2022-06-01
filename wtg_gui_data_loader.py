# -*- coding: utf-8 -*-
"""

@author: follettt
"""
## Constants
LOCALDIR = 'C:\Database\WTG'
# USER = ''  Secrets file
BOXDIR = 'C:\\Users\\follettt\\Box\\WHET_LAB\\data\\MMIData Server\\Database'
#PROJECTS = '\\'.join([LOCALDIR, 'wtg_project_list.csv'])
PROJECTS = '\\'.join([BOXDIR, 'wtg_project_list.csv'])
SEL_DATA = 'C:\\Database\\WTG\\wtg_project_list.csv'
ISO_DATA = 'C:\\Database\\WTG\\test_isotope.csv'
LOC_DATA = 'C:\\Database\\WTG\\encounter.csv'


class encounter(object):
    encounter = ''
    enc_argos = ''
    enc_biopsy = ''
    enc_deploy = ''
    enc_fastloc = ''
    enc_photo = ''

class metadata(object):
    animal_meta = ''
    tag_meta = ''

class tag_data(object):
    tel_beh = 'tag_data_tel_behavior.csv'
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
    

## SelectBox Dicts / Lists
class select_box(object):
    species = ['Blue',
               'Bowhead',
               'Bryde',
               'Gray',
               'HybridBF',
               'Humpback',
               'RightN',
               'RightS',
               'Sperm']

    loc_types = {'Argos':'argos', 
                 'FastLoc':'fastloc',
                 'Deployment':'deploy',
                 'Biopsy':'biopsy',
                 'Photo-ID':'photo'}
    
    bio_types = ['Hormones',
                 'Stable Isotopes',
                 'What else?']
    
    tag_types =  {'Location Only':'LO',
                  'Dive Summary':'DS',
                  'Dive Measurement': 'DM',
                  'Adv. Dive Behavior':'ADB'}
    
    
    
    