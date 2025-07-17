'''
@author: Jack Charles   https://jackcharlesconsulting.com/
'''

import math
import json
import numpy as np
import matplotlib.pyplot as plt
import util.wellengcalc as wec

class PipeEnvelope():
    def __init__(self, name:str, description:str, tubing_od:float, tubing_id:float, radius:float, eccentricity:float, 
                 temperature:float, yield_point:float, Youngs_modulus:float, Poissons_ratio:float, 
                 DF_burst_triaxial:float, DF_tension_triaxial:float, DF_burst:float, DF_collapse:float, DF_tension:float, 
                 VME_tension:list[float], VME_pressure:list[float], API_burst:float, API_collapse:float, API_tension:float):
        self.name = name
        self.description = description
        self.tubing_od = tubing_od
        self.tubing_id = tubing_id
        self.radius = radius
        self.eccentricity = eccentricity
        self.temperature = temperature
        self.yield_point = yield_point
        self.Youngs_modulus = Youngs_modulus
        self.Poissons_ratio = Poissons_ratio
        self.DF_burst_triaxial = DF_burst_triaxial
        self.DF_tension_triaxial = DF_tension_triaxial
        self.DF_burst = DF_burst
        self.DF_tension = DF_tension
        self.DF_collapse = DF_collapse
        self.VME_tension = VME_tension
        self.VME_pressure = VME_pressure
        self.API_burst = API_burst
        self.API_collapse = API_collapse
        self.API_tension = API_tension

    def calc_VME_API_curves(self):
        self.VME_pressure, self.VME_tension = wec.calc_VM_envelope(self.tubing_od, self.tubing_id, self.yield_point, self.radius, self.eccentricity, self.temperature, self.DF_burst_triaxial, self.DF_tension_triaxial)
        self.API_collapse = wec.calc_API_collapse(self.tubing_od, self.tubing_id, self.yield_point, self.Youngs_modulus, self.Poissons_ratio, self.temperature) / self.DF_collapse
        self.API_burst = wec.calc_API_burst(self.tubing_od, self.tubing_id, self.yield_point) * wec.calc_pipe_temperature_derating(self.temperature) / self.DF_burst
        self.API_tension = wec.calc_API_tensile(self.tubing_od, self.tubing_id, self.yield_point) * wec.calc_pipe_temperature_derating(self.temperature)  / self.DF_tension

class CaTStressAnalysisResults():
    def __init__(self, CAT_load_name:str, tension:list[float], pressure:list[float]):
        self.CAT_load_name = CAT_load_name
        self.tension = tension
        self.pressure = pressure

def import_CAT_data_file(data_filename:str, CAT_load_name:str):
    data_ndarray = np.genfromtxt(data_filename, delimiter=',', dtype=float, skip_header=1)  
    data_class, _x, _tens, _press = [], [], [], []
    for data_content in data_ndarray:
        _x = data_content.tolist()
        _tens.append(_x[0])
        _press.append(_x[1])
    data_class = CaTStressAnalysisResults(CAT_load_name, _tens, _press)
    return data_class

def plot_VME(VME_data:dict[str,PipeEnvelope], CAT_data:dict[str,CaTStressAnalysisResults]):
    fig = plt.figure()
    fig.suptitle("VME Plot")
    fig.tight_layout()

    ax1 = fig.add_subplot(111)
    
    for _x in VME_data.keys():
        ax1.plot(VME_data[_x].VME_tension, VME_data[_x].VME_pressure, label = VME_data[_x].name)
        API_x = [VME_data[_x].API_tension, VME_data[_x].API_tension, 0, -VME_data[_x].API_tension, -VME_data[_x].API_tension, VME_data[_x].API_tension]
        API_y = [VME_data[_x].API_burst, 0, -VME_data[_x].API_collapse, -VME_data[_x].API_collapse, VME_data[_x].API_burst, VME_data[_x].API_burst]
        ax1.plot(API_x, API_y, color='black')
        
        ax1.annotate(xy = (0,max(VME_data[_x].VME_pressure)), text = f"Triaxial DF={VME_data[_x].DF_burst_triaxial}", horizontalalignment = 'center', verticalalignment = 'bottom', fontsize = 6)
        ax1.annotate(xy = (-VME_data[_x].API_tension,VME_data[_x].API_burst), text = f"Burst DF={VME_data[_x].DF_burst}", horizontalalignment = 'left', verticalalignment = 'bottom', fontsize = 6)
        ax1.annotate(xy = (VME_data[_x].API_tension,0), text = f"Tension DF={VME_data[_x].DF_tension}", horizontalalignment = 'right', verticalalignment = 'bottom', fontsize = 6)
        ax1.annotate(xy = (0,-VME_data[_x].API_collapse), text = f"Collapse DF={VME_data[_x].DF_collapse}", horizontalalignment = 'right', verticalalignment = 'bottom', fontsize = 6)
    
    #for _x in CXN_data.keys():
    #    ax1.plot(CXN_data[_x].tension, CXN_data[_x].pressure, label = CXN_data[_x].CXN_name)

    for _x in CAT_data.keys():
        ax1.plot(CAT_data[_x].tension, CAT_data[_x].pressure, label = CAT_data[_x].CAT_load_name)
    
    ax1.set_xlabel("Tension")
    ax1.set_ylabel("Pressure")
    ax1.legend(loc='best', fontsize=8)
    ax1.grid(True)

    plt.show()  
