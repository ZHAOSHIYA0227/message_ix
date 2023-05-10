import pandas as pd
import ixmp 
import message_ix
import matplotlib.pyplot as plt

from message_ix.utils import make_df
# We import a utility function called make_df, which can be used to wrap the input data into dataframes that can be saved in model parameters.
# %matplotlib inline

# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible.
## But I don't understand this line. 
# Python Arithmetic Operators
# + Addition; - subtraction; * multiplication; / division; 
# % modulus; ** exponentiation; // floor division. 

mp = ixmp.Platform()
#---- ERROR MESSAGE ----
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/opt/homebrew/lib/python3.10/site-packages/ixmp/core/platform.py", line 92, in __init__
#   self._backend = backend_class(**kwargs)
#   File "/opt/homebrew/lib/python3.10/site-packages/ixmp/backend/jdbc.py", line 235, in __init__
#     start_jvm(jvmargs)
#   File "/opt/homebrew/lib/python3.10/site-packages/ixmp/backend/jdbc.py", line 1191, in start_jvm
#     log.debug(f"jpype.getDefaultJVMPath: {jpype.getDefaultJVMPath()}")
#   File "/opt/homebrew/lib/python3.10/site-packages/jpype/_jvmfinder.py", line 74, in getDefaultJVMPath
#     return finder.get_jvm_path()
#   File "/opt/homebrew/lib/python3.10/site-packages/jpype/_jvmfinder.py", line 212, in get_jvm_path
#     raise JVMNotFoundException("No JVM shared library file ({0}) "
# jpype._jvmfinder.JVMNotFoundException: No JVM shared library file (libjli.dylib) found. Try setting up the JAVA_HOME environment variable properly.

# TO solve the issue above, check the Java installation and versions
# TO install JAVA on MacOS ventura, see https://www.google.com/search?q=java+installation+mac+ventura&rlz=1C5CHFA_enJP989JP989&oq=java+installation+mac+ventura&aqs=chrome..69i57j33i160l3j33i22i29i30l6.7487j0j4&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:9bdb4b47,vid:uDK_GWfTvmU 
# In the tutorial above, vim text editor is used. To save the changes after editing the text, press ESC and type ":wq!".

# ---- Creating a new scenario ---- #
scenario = message_ix.Scenario(
    mp, model="Westeros Electrified", scenario="baseline", version="new"
)

# message_ix.Scenario() defines scenario, which is a TimeSeries variable in MESSAGEix


#---- Model structure ----#
# defining basic characteristics of the model, including time, space, and the energy system structure
history = [690]  # a list with an integer, time periods in history
model_horizon = [700, 710, 720]  # a list with 3 integers, time periods inmodel horizon
scenario.add_horizon(year = history + model_horizon, firstmodelyear = model_horizon[0])  
# what is the model concept of "node"

#---- Fill in the energy system's settings ----#
country = "Westeros"   # string, or a list of strings 
scenario.add_spatial_sets({"country": country})

scenario.add_set("commodity", ["electricity", "light"]) # scenario.add_set("setName",[A list of strings to put into the set])
scenario.add_set("level", ["secondary", "final", "useful"]) 
scenario.add_set("technology", ["coal_ppl", "wind_ppl", "grid", "bulb"]) 
scenario.add_set("mode", ["standard"]) 

#---- Balancing commodities ----#
gdp_profile = pd.Series([1.0, 1.5, 1.9], index = pd.Index(model_horizon, name = "Time")) # the index of list are 0 based 
gdp_profile.plot(title= "GDP profile")

# demand must be met, and supply can exceed demand allowing the model to plan for meeting demand in future periods by storing storable commodities. 

demand_per_year = 40 * 12 * 1000 /8760
# 40 million people 
# 12 being the factor of population growth
# 1000 kWh electricity per capita demand (per year?)
# 8760 hours in a year
light_demand = pd.DataFrame(
    {
        "node": country,    # what is the concept of node?
        "commodity": "light",
        "level": "useful", 
        "year": model_horizon,
        "time": "year",
        "value": (demand_per_year * gdp_profile).round(),
        "unit": "GWa",
    }
)

# The light_demand shows the data format (pandas.DataFrame) for MESSAGEix. 
# The dataframe definition: pd.DataFrame({ "colName1": contents, "colName2": contents, "colName3": contents,})

#---- Defining the input  and output commodities of each technology ----#
# Input quantities require _origin keys that specify where the inputs are received from.
# Output quantities require _dest keys that specify where the outputs are transferred to.

year_df = scenario.vintage_and_active_years()
vintage_years, act_years = year_df["year_vtg"], year_df["year_act"]

# Some common values to be used for both the "input" and "output" parameters
base = dict(
    node_loc=country,
    year_vtg=vintage_years,
    year_act=act_years,
    mode="standard",
    time="year",
    unit="-",
)
# dict() is the dictionary variable, which is a variable container model. It acommodates any type of elements. 

# Use the message_ix utility function make_df() to create a base data frame for
# different "input" parameter values
base_input = make_df("input", **base, node_origin=country, time_origin="year")

# Create a base data frame for different "output" parameter values
base_output = make_df("output", **base, node_dest=country, time_dest="year")


#----------------------------------#
#---- An example of light bulb ----#
#----------------------------------#

#---- the input and output of a light bulb ----#
# A light bulb…
# --> receives "input" in the form of the "electricity" commodity at the "final" energy level, and
# --> "output"s the commodity "light" at the "useful" energy level.
# The value in the input and output parameter is used to represent t                                              he efficiency of a technology (efficiency = output/input). For example, input of 1.0 and output of 1.0 for a technology shows that the efficiency of that technology is 100% in converting the input commodity to the output commodity.

# Extend "base_output" by filling in some of the other columns with keys, using the pandas.DataFrame.assign() method. 
bulb_out = base_output.assign(
    technology = "bulb", commodity = "light", level = "useful", value = 1.0
)

# index=scenario.index
# print(index)
scenario.add_par("output", bulb_out)   # adding parameter "bulb_out" in scenario

bulb_in = base_input.assign(
    technology = "bulb",
    commodity = "electricity", 
    level = "final", 
    value = 1.0
)
scenario.add_par("input", bulb_in)

# If you don't know the dimensions for a specific parameter—in other words, which keyword arguments you need to pass to make_df(), you can use Scenario.idx_names(DataFrame):

#--------------------------------------------------#
#---- Parameterization of the electrical grid ----#
#--------------------------------------------------# 
# it receives electricity at the  "secondary" energy level
# it outputs electricity at the "final" energy level 

grid_efficiency = 0.9
grid_out = base_output.assign(
    technology="grid",
    commodity="electricity",
    level="final",
    value=grid_efficiency,
)
scenario.add_par("output", grid_out)

grid_in = base_input.assign(
    technology="grid", commodity="electricity", level="secondary", value=1.0
)
scenario.add_par("input", grid_in)

# The model does not include the fossil resources used as "input" for coal plants; however, costs of coal extraction are included in the parameter  var_cost.
# output from coal power plants
coal_out = base_output.assign(
    technology="coal_ppl",
    commodity="electricity",
    level="secondary",
    value=1.0,
    unit="GWa",
)
scenario.add_par("output", coal_out)

# output from wind power plants
wind_out = base_output.assign(
    technology="wind_ppl",
    commodity="electricity",
    level="secondary",
    value=1.0,
    unit="GWa",
)
scenario.add_par("output", wind_out)

#---- operational constraints on the power plants ----#
# reality constraints: relate built capacity (CAP) to available power/ the activity (ACT) of that technology. 
# Call make_df() and add_par() in a loop to execute similar code for three technologies:
capacity_factor = {
    "coal_ppl": 1,
    "wind_ppl": 0.36,
    "bulb": 1,
}

for tec, val in capacity_factor.items():
    df = make_df(
        "capacity_factor",
        node_loc = country,
        year_vtg = vintage_years,
        year_act = act_years,
        time = "year",
        unit = "-",
        technology = tec,
        value = val,
    )
    scenario.add_par("capacity_factor", df)

# a dataframe for technical lifetime
lifetime = {
    "coal_ppl": 20,
    "wind_ppl": 20,
    "bulb": 1,
}

for tec, val in lifetime.items():
    df = make_df(
        "technical_lifetime",
        node_loc = country,
        year_vtg = model_horizon,
        unit = "y",
        technology = tec, 
        value = val,
    )
    scenario.add_par("technical_lifetime", df)



#---- Technical diffusion and contraction ----#
# Energy systems can not be transformed instantaneously. We use a family of dynamic constraints on activity and capacity. 
# These constraints define the upper and lower limit of the domain of activity and capacity over time based on their value in the previous time step, an initial value, and growth/decline rates.

growth_technologies = [
    "coal_ppl",
    "wind_ppl",
]

for tec in growth_technologies: 
    df = make_df(
        "growth_activity_up",
        node_loc = country,
        year_act = model_horizon,
        time = "year",
        unit = "-",
        technology = tec, 
        value = 0.1,
    )
    scenario.add_par("growth_activity_up", df)


historic_demand = 0.5 * demand_per_year
historic_generation = historic_demand / grid_efficiency
coal_fraction = 0.6

old_activity = {
    "coal_ppl": coal_fraction * historic_generation,
    "wind_ppl": (1 - coal_fraction) * historic_generation,
}

for tec in old_activity:
    value = old_activity[tec]/(1*10*capacity_factor[tec])
    df = make_df(
        "historical_new_capacity",
        node_loc =country,
        year_vtg =history,
        unit = "GWa",
        technology = tec,
        value = value,
    )


#---- Defining the energy mix ----#
# the existing energy system is defined by parameters "historical_activity", "historical_new_capacity" before the model horizon. 
# key values to be defined: 

historic_demand = 0.5 * demand_per_year  # how much useful energy was needed
historic_generation = historic_demand / grid_efficiency   # how much finalenergy was generated
coal_fraction = 0.6  # the mix for different technologies

old_activity = {
    "coal_ppl": coal_fraction * historic_generation,
    "wind_ppl": (1-coal_fraction)*historic_generation,
}

for tec,val in old_activity.items():
    df = make_df(
        "historical_activity",
        node_loc = country,
        year_act = history,
        mode = "standard", 
        time = "year",
        unit = "GWa",
        technology = tec, 
        value = val,
    )
    scenario.add_par("historical_activity", df)


#----------------------------#
#---- Objective function ----#
#----------------------------#

# interest rate
scenario.add_par("interestrate", model_horizon, value = 0.05, unit = "-")

# investment costs
# Add a new unit for ixmp to recognize as valid
mp.add_unit("USD/kW")

# in $ / kW (specific investment cost)
costs = {
    "coal_ppl": 500,
    "wind_ppl": 1500,
    "bulb": 5,
}

for tec, val in costs.items():
    df = make_df(
        "inv_cost",
        node_loc=country,
        year_vtg=model_horizon,
        unit="USD/kW",
        technology=tec,
        value=val,
    )
    scenario.add_par("inv_cost", df)


# Fixed O & M costs
# In $ / kWa (costs associated with the degradation of equipment
# when the plant is functioning per unit of energy produced
# kW·year = 8760 kWh. Therefore the costs represents USD per 8760 kWh
# of energy). Do not confuse with fixed O&M units.

costs = {
    "coal_ppl": 30,
    "grid": 50,
}

for tec, val in costs.items():
    df = make_df(
        "var_cost",
        node_loc=country,
        year_vtg=vintage_years,
        year_act=act_years,
        mode="standard",
        time="year",
        unit="USD/kWa",
        technology=tec,
        value=val,
    )
    scenario.add_par("var_cost", df)



#-----------------------#
#---- Solving model ----#
#-----------------------#
from message_ix import log

log.info(f"version number before commit(): {scenario.version}")

scenario.commit(comment="basic model of Westeros electrification")

log.info(f"version number after commit(): {scenario.version}")

#  log.info(f "version number before commit(): {scenario.version}")
# scenario.commit(comment = "basic model of Westeros  electrification")
# log.info(f "version number after commit(): {scenario.version}")

# setting a default scenario version as if loaded from the ixmp database
scenario.set_as_default()
scenario.solve()
scenario.var("OBJ")["lvl"]


# #---------------------------#
# #---- reporting results ----#
# #---------------------------#
# # Create a Reporter object to describe and carry out reporting
# # calculations and operations (like plotting) based on `scenario`
from message_ix.reporting import Reporter

rep = Reporter.from_scenario(scenario)

# # "prepare_plots" enables several to describe reporting operations, e.g.
# # "plot activity", "plot capacity", or "plot prices"
# # See message_ix/util/tutorial.py for more information
from message_ix.util.tutorial import prepare_plots

prepare_plots(rep)


# #---- Activity ----#
# # Only show a subset of technologies in the following plots;
# # e.g. exclude "bulb" and "grid"
rep.set_filters(t=["coal_ppl", "wind_ppl"])

# # Trigger the calculation and plotting
rep.get("plot activity")


# #---- New capacity ----#
# # Create a different plot. The same filters are still active.
rep.get("plot capacity")


# #---- Energy Price ----#
# # Replace the technology filters with a commodity filter;
# # show only "light" and not e.g. "electricity".
rep.set_filters(c=["light"])

# # Create a price plot
# rep.get("plot prices")


# #---- Closing the database connection ----#
mp.close_db()


plt.show()