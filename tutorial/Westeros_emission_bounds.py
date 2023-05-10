import pandas as pd
import ixmp 
import message_ix
import matplotlib.pyplot as plt
import pathlib 
import os

from message_ix.util import make_df

#---- Loading modeling platform ----#
mp = ixmp.Platform()

# os.chdir("tutorial/westeros/")
# os.chdir(__file__)
system_path11 = os.getcwd()
print("system path")
print(system_path11)


# making a clone of the existing scenario "baseline"
model = "Westeros Electrified"

# Loading the Westeros baselins scenario 
base = message_ix.Scenario(mp, model = model, scenario = "baseline")
scen = base.clone(
    model, 
    "emission_bound",
    "introducing an upper bound on emissions",
    keep_solution = False,
)
scen.check_out()

year_df = scen.vintage_and_active_years()
vintage_years, act_years = year_df["year_vtg"], year_df["year_act"]
model_horizon = scen.set("year")
country = "Westeros"

# introducing emissions
# the emission of CO2 and the emission category GHG
scen.add_set("emission", "CO2")
scen.add_cat("emission", "GHG", "CO2")

# new units to the model library
mp.add_unit("tCO2/kWa")
mp.add_unit("MtCO2")

# add CO2 emissions to the coal powerplant
emission_factor = make_df(
    "emission_factor",
    node_loc = country,
    year_vtg = vintage_years,
    year_act = act_years,
    mode = "standard",
    unit = "tCO2/kWa",
    technology = "coal_ppl",
    emission ="CO2",
    value = 7.4
)
scen.add_par("emission_factor", emission_factor)


# Bound on emissions
scen.add_par(
    "bound_emission",
    [country, "GHG", "all", "cumulative"], value = 500.0, unit = "MtCO2"
)

# solving the model
scen.commit(comment = "Introducing emissions and setting an upper bound") # what does "scen.commit" mean??
scen.set_as_default()

scen.solve()

scen.var("OBJ")["lvl"]  # check the level of the gams variable "OBJ"


#---- Plotting ----#
from message_ix.reporting import Reporter
from message_ix.util.tutorial import prepare_plots

rep = Reporter.from_scenario(scen)
prepare_plots(rep)

# Activity
rep.set_filters(t = ["coal_ppl","wind_ppl"])
rep.get("plot activity")

# Capacity
rep.get("plot capacity")

# Electricity price
# the marginal cost of electricity generation, which is in fact the marginal cost of the most expensive generator. 

# rep.set_filters(t = None, c = ["light"])
# rep.get("plot prices")

mp.close_db()


plt.show()


