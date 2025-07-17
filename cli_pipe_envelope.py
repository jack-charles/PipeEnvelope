'''
@author: Jack Charles   https://jackcharlesconsulting.com/
'''

import math
import json
import numpy as np
import matplotlib.pyplot as plt
import util.wellengcalc as wec
import calcs.pipe_envelope as penv


VME_data = {}
load_data = {}
menu_loop = True

while menu_loop != False:
    print(f"\nCurrent Units are psi and inches")
    menu_selection = int(input(f"Please type the number of selection\n"
                        "1: Input Pipe Data\n"
                        "2: Add Data Points\n"
                        "3: Plot VME Graphs\n"
                        "0: Quit\n"
                        "Selection: "))
    
    if menu_selection == 1:
        name = input("Name/Description of VME Plot: ")
        tubing_od = float(input("Pipe OD: "))
        tubing_id = float(input("Pipe ID: "))
        eccentricity = float(input("Wall thickness or eccentricity (fraction): "))
        yield_point = float(input("Minimum Yield Stress: "))
        Youngs_modulus = float(input("Young's Modulus: "))
        Poissons_ratio = float(input("Poisson's Ratio: "))
        temperature = float(input("Temperature: "))
        radial_stress_query = input("Include radial stresses? (Y/N): ")
        
        DF_burst_triaxial = float(input("Design Factor Triaxial Burst: "))
        DF_tension_triaxial = float(input("Design Factor Triaxial Tension: "))
        DF_burst = float(input("Design Factor Burst: "))
        DF_collapse = float(input("Design Factor Collapse: "))
        DF_tension = float(input("Design Factor Tension: "))
        
        if radial_stress_query == "Y":
            radius = tubing_id/2
        else:
            radius = tubing_od/2
        
        VME_data[name]= penv.PipeEnvelope(name, "", tubing_od, tubing_id, radius, eccentricity, temperature, yield_point, Youngs_modulus, Poissons_ratio,
                                                  DF_burst_triaxial, DF_tension_triaxial, DF_burst, DF_collapse, DF_tension,
                                                  [],[],0,0,0)
        VME_data[name].calc_VME_API_curves()
        print(VME_data.keys())       
    elif menu_selection == 2:
        load_name = input("Name of load case: ")
        stress_data_filename = input("Path to Stress Results: ")
        try:
            load_data[load_name] = penv.import_CAT_data_file(stress_data_filename, load_name)
        except FileNotFoundError:
            print("File not found")      
    
    elif menu_selection == 3:
        penv.plot_VME(VME_data, load_data)
      
    elif menu_selection == 0:
        print("Thank you")
        menu_loop = False



#Demo mode 1 for testing
    elif menu_selection == 10:
        name = "w/o Radial Stress"
        tubing_od = 5.5
        tubing_id = 4.995
        eccentricity = 0.875
        yield_point = 80000.0
        Youngs_modulus = 30.0*10**6
        Poissons_ratio = 0.25
        temperature = 75.0
        radial_stress_query = "N"
        
        DF_burst_triaxial = 1.0
        DF_tension_triaxial = 1.0
        DF_burst = 1.0
        DF_collapse = 1.0
        DF_tension = 1.0

        if radial_stress_query == "Y":
            radius = tubing_id/2
        else:
            radius = tubing_od/2

        VME_data[name] = penv.PipeEnvelope(name, "", tubing_od, tubing_id, radius, eccentricity, temperature, yield_point, Youngs_modulus, Poissons_ratio,
                                                  DF_burst_triaxial, DF_tension_triaxial, DF_burst, DF_collapse, DF_tension,
                                                  [],[],0,0,0)
        VME_data[name].calc_VME_API_curves()
        print(VME_data.keys())

        penv.plot_VME(VME_data, load_data)