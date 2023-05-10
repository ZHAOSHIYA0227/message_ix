import pandas as pd
import ixmp 
import message_ix
import matplotlib.pyplot as plt


#---- Loading modeling platform ----#
mp = ixmp.Platform()

#---- Loading the Westeros baselins scenario ----#
base = message_ix.Scenario(mp, model = "Westeros Electrified", scenario = "baseline")

# Export the data to a file called westeros_baseline_data.xlsx
data_file = "westeros_baseline_data.xlsx"
base.to_excel(data_file)

#---- Create a new scenario ----#
scenario = message_ix.Scenario(
    mp, model = "Westeros Electrified", scenario = "baseline_xlsx", version = "new"
)


#---- Importing data rom Excel ----#
# Instead of using the message_ix.Scenario.add_par() for adding data to a MESSAFEix parameter, we import data from an Excel data.
# The argument "add_units" has been set to "True", so that any units which have not yet been specified in the modeling platform will be defined automatically.
scenario.read_excel(data_file, add_units=True)

#---- Solve the model ----#
scenario.set_as_default()
scenario.solve()

#---- check the objective value ----#
# Objective value of the original 'baseline' scenario
base.var("OBJ")["lvl"]

# Objective value of scenario built using the Excel file
scenario.var("OBJ")["lvl"]

mp.close_db()

plt.show()


# ERROR
# 2023-04-06 20:05:59,083 ERROR at.ac.iiasa.ixmp.objects.Scenario:1691 - variable 'I' not found in gdx!
# 2023-04-06 20:05:59,084 ERROR at.ac.iiasa.ixmp.objects.Scenario:1691 - variable 'C' not found in gdx!