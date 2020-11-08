import numpy
import pandas as pd


"""
    This module takes in the input from index page and returns the json values
 """

def wind_maintenance(wind_path):
    """ Function reads the csvfile of the maintenance data 
    """
    wind_data=pd.read_csv(wind_path)
    return()
    
def solar_maintenance(solar_path):
    """ Function reads the csvfile of the maintenance data """
    solar_data=pd.read_csv(solar_path)
    print(solar_data)
    return()