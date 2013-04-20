"""
Configuration file of JARVIS
"""

TRACKER_COLOR={'MIN':[20,100,100],'MAX':[30,255,255]}
GESTURE_COLOR={'MIN': [108.0, 100, 10],'MAX': [118.0, 255, 255]}
RESOLUTION=[1366,768]
SCALE_FACTOR=1+0.2
MANUAL_CONFIGURATION=False
"""
    ADVANCED CONFIGURATION. DONT EDIT IT IF YOU ARE NOT SURE
"""
#Gesture settings
GRID_NUM=5
ALLOWANCE=0.05 #5% of grid size
MIN_GRID_SIZE=25

#Database
DB="data/gestures.db"
DB_MASTER="data/gestures_master.db"
ANALYZE_JSON="data/analyzer.JSON"
RES="res/"

#Working Directory
CWD='/home/alse/alse_python/jarvis/'

#DONT EDIT THIS
DB=CWD+DB
DB_MASTER=CWD+DB_MASTER
ANALYZE_JSON=CWD+ANALYZE_JSON
RES=CWD+RES

"""
    GUI configuration
"""
WINDOW_ID="Jarvis"
OPACITY=0.9
ALWAYS_ON_TOP=True
ON_ALL_WORKSPACES=True
