import pandas as pd
import ixmp 
import message_ix
import matplotlib.pyplot as plt
import pathlib 
import os

# os.chdir("tutorial/westeros/")
# os.chdir(__file__)
system_path11 = os.getcwd()
print("system path")
print(system_path11)
#---- Loading modeling platform ----#
mp = ixmp.Platform()

#---- Loading the Westeros baselins scenario ----#
base = message_ix.Scenario(mp, model = "Westeros Electrified", scenario = "baseline")

# Export the data to a file called westeros_baseline_data.xlsx
# data_file = "tutorial\westeros\westeros_baseline_data.xlsx"
data_file = "tutorial\westeros\westeros_baseline_data.xlsx"
base.to_excel(data_file)

#---- Create a new empty scenario ----#
scenario = message_ix.Scenario(
    mp, model = "Westeros Electrified", scenario = "baseline_xlsx", version = "new"
)


#-------------------------#
#---- Model structure ----#
#-------------------------#

# Defining basic characteristics of the model, including time, space, and the energy system structure
history = [690]  # a list with an integer, time periods in history
model_horizon = [700, 710, 720]  # a list with 3 integers, time periods inmodel horizon
scenario.add_horizon(year = history + model_horizon, firstmodelyear = model_horizon[0])  
# what is the model concept of "node"

# Defining a spatial level and adding a node to it
node = "Westeros"   # string, or a list of strings 
scenario.add_spatial_sets({"country": node})

# Adding elements to MESSAGEix sets
scenario.add_set("commodity", ["electricity", "light"]) # scenario.add_set("setName",[A list of strings to put into the set])
scenario.add_set("level", ["secondary", "final", "useful"]) 

# Adding interest rate of 5% per model year
scenario.add_par("interestrate", model_horizon, value = 0.05, unit = "-")

#-----------------------------------#
#---- Importing data from excel ----#
#-----------------------------------#
from pathlib import Path

# data_folder = Path("tutorial/")
# file_to_open = data_folder/"westeros_baseline_demand.xlsx"
file_to_open = "tutorial\westeros\westeros_baseline_demand.xlsx"
scenario.read_excel(file_to_open, add_units=True, commit_steps=False)
# scenario.read_excel("tutorial\westeros\westeros_baseline_demand.xlsx", add_units=True, commit_steps=False)
print(scenario.idx_names("demand"))


# Adding technologies
scenario.read_excel(
    "tutorial\westeros\westeros_baseline_technology_basic.xlsx", add_units=True, commit_steps=False
)
scenario.set("technology")
scenario.par("capacity_factor")

# Technological diffusion and contraction
# an initial definition of technologies is given above. We will add parameters for already defined technologies. We import the parameter "growth_activity_up" from "tutorial\westeros\westeros_baseline_technology_constraint.xlsx"
scenario.read_excel(
    "tutorial\westeros\westeros_baseline_technology_constraint.xlsx", add_units=True, commit_steps=False
)

# Defining an Energy Mix
# Importing data of the historical years
scenario.read_excel(
    "tutorial\westeros\westeros_baseline_technology_historic.xlsx", add_units=True, commit_steps=False
)

# Investment, fixed O&M, and variable O&M costs
scenario.read_excel(
    "tutorial\westeros\westeros_baseline_technology_economic.xlsx", add_units=True, commit_steps=False
)


# Solving the model 
scenario.set_as_default()
scenario.solve()

#---- check the objective value ----#
# Objective value of the original 'baseline' scenario
base=message_ix.Scenario(mp, model = "Westeros Electrified", scenario="baseline")
base.var("OBJ")["lvl"]

# Objective value of scenario built using the Excel file
scenario.var("OBJ")["lvl"]

mp.close_db()


plt.show()


# ERROR 
# 2023-04-06 21:21:34,428 ERROR at.ac.iiasa.ixmp.objects.Scenario:1691 - variable 'I' not found in gdx!
# 2023-04-06 21:21:34,428 ERROR at.ac.iiasa.ixmp.objects.Scenario:1691 - variable 'C' not found in gdx!