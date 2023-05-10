
# import ixmp 
# import message_ix
import matplotlib.pyplot as plt
# import xlrd
import openpyxl
import gdxpds
import pandas as pd

input = "../xlsx/MESSAGEix-GLOBIOM 1.1-R12_baseline_DEFAULT.xlsx"

#---- set -----#
df_balance_equality = pd.read_excel(input, sheet_name="balance_equality")
print(df_balance_equality)
type(df_balance_equality)
df_balance_equality.insert(df_balance_equality.shape[1],"gdxtime", "True")
print(df_balance_equality)

df_cat_emission = pd.read_excel(input, sheet_name="cat_emission")
print(df_cat_emission)
type(df_cat_emission)
df_cat_emission.insert(df_cat_emission.shape[1],"gdxtime", "True")
print(df_cat_emission)

df_cat_node = pd.read_excel(input, sheet_name="cat_node")
print(df_cat_node)
type(df_cat_node)
df_cat_node.insert(df_cat_node.shape[1],"gdxtime", "True")
print(df_cat_node)

df_cat_tec = pd.read_excel(input, sheet_name="cat_tec")
print(df_cat_tec)
type(df_cat_tec)
df_cat_tec.insert(df_cat_tec.shape[1],"gdxtime", "True")
print(df_cat_tec)

df_cat_year = pd.read_excel(input, sheet_name="cat_year")
print(df_cat_year)
type(df_cat_year)
df_cat_year.insert(df_cat_year.shape[1],"gdxtime", "True")
print(df_cat_year)

df_commodity = pd.read_excel(input, sheet_name="commodity")
print(df_commodity)
type(df_commodity)
df_commodity.insert(df_commodity.shape[1],"gdxtime", "True")
print(df_commodity)


df_emission = pd.read_excel(input, sheet_name="emission")
print(df_emission)
type(df_emission)
df_emission.insert(df_emission.shape[1],"gdxtime", "True")
print(df_emission)

df_grade = pd.read_excel(input, sheet_name="grade")
print(df_grade)
type(df_grade)
df_grade.insert(df_grade.shape[1],"gdxtime", "True")
print(df_grade)


df_land_scenario = pd.read_excel(input, sheet_name="land_scenario")
print(df_land_scenario)
type(df_land_scenario)
df_land_scenario.insert(df_land_scenario.shape[1],"gdxtime", "True")
print(df_land_scenario)

df_land_type = pd.read_excel(input, sheet_name="land_type")
print(df_land_type)
type(df_land_type)
df_land_type.insert(df_land_type.shape[1],"gdxtime", "True")
print(df_land_type)

df_level = pd.read_excel(input, sheet_name="level")
print(df_level)
type(df_level)
df_level.insert(df_level.shape[1],"gdxtime", "True")
print(df_level)

df_level_resource = pd.read_excel(input, sheet_name="level_resource")
print(df_level_resource)
type(df_level_resource)
df_level_resource.insert(df_level_resource.shape[1],"gdxtime", "True")
print(df_level_resource)


df_level_stocks = pd.read_excel(input, sheet_name="level_stocks")
print(df_level_stocks)
type(df_level_stocks)
df_level_stocks.insert(df_level_stocks.shape[1],"gdxtime", "True")
print(df_level_stocks)

df_lvl_spatial = pd.read_excel(input, sheet_name="lvl_spatial")
print(df_lvl_spatial)
type(df_lvl_spatial)
df_lvl_spatial.insert(df_lvl_spatial.shape[1],"gdxtime", "True")
print(df_lvl_spatial)

df_lvl_temporal = pd.read_excel(input, sheet_name="lvl_temporal")
print(df_lvl_temporal)
type(df_lvl_temporal)
df_lvl_temporal.insert(df_lvl_temporal.shape[1],"gdxtime", "True")
print(df_lvl_temporal)

df_map_node = pd.read_excel(input, sheet_name="map_node")
print(df_map_node)
type(df_map_node)
df_map_node.insert(df_map_node.shape[1],"gdxtime", "True")
print(df_map_node)


df_map_spatial_hierarchy = pd.read_excel(input, sheet_name="map_spatial_hierarchy")
print(df_map_spatial_hierarchy)
type(df_map_spatial_hierarchy)
df_map_spatial_hierarchy.insert(df_map_spatial_hierarchy.shape[1],"gdxtime", "True")
print(df_map_spatial_hierarchy)


df_map_temporal_hierarchy = pd.read_excel(input, sheet_name="map_temporal_hierarchy")
print(df_map_temporal_hierarchy)
type(df_map_temporal_hierarchy)
df_map_temporal_hierarchy.insert(df_map_temporal_hierarchy.shape[1],"gdxtime", "True")
print(df_map_temporal_hierarchy)


df_map_time = pd.read_excel(input, sheet_name="map_time")
print(df_map_time)
type(df_map_time)
df_map_time.insert(df_map_time.shape[1],"gdxtime", "True")
print(df_map_time)


df_mapping_macro_sector = pd.read_excel(input, sheet_name="mapping_macro_sector")
print(df_mapping_macro_sector)
type(df_mapping_macro_sector)
df_mapping_macro_sector.insert(df_mapping_macro_sector.shape[1],"gdxtime", "True")
print(df_mapping_macro_sector)


df_mode = pd.read_excel(input, sheet_name="mode")
print(df_mode)
type(df_mode)
df_mode.insert(df_mode.shape[1],"gdxtime", "True")
print(df_mode)


df_node = pd.read_excel(input, sheet_name="node")
print(df_node)
type(df_node)
df_node.insert(df_node.shape[1],"gdxtime", "True")
print(df_node)

df_rating = pd.read_excel(input, sheet_name="rating")
print(df_rating)
type(df_rating)
df_rating.insert(df_rating.shape[1],"gdxtime", "True")
print(df_rating)


df_relation = pd.read_excel(input, sheet_name="relation")
print(df_relation)
type(df_relation)
df_relation.insert(df_relation.shape[1],"gdxtime", "True")
print(df_relation)


df_sector = pd.read_excel(input, sheet_name="sector")
print(df_sector)
type(df_sector)
df_sector.insert(df_sector.shape[1],"gdxtime", "True")
print(df_sector)


df_technology = pd.read_excel(input, sheet_name="technology")
print(df_technology)
type(df_technology)
df_technology.insert(df_technology.shape[1],"gdxtime", "True")
print(df_technology)

df_time = pd.read_excel(input, sheet_name="time")
print(df_time)
type(df_time)
df_time.insert(df_time.shape[1],"gdxtime", "True")
print(df_time)


df_type_emission = pd.read_excel(input, sheet_name="type_emission")
print(df_type_emission)
type(df_type_emission)
df_type_emission.insert(df_type_emission.shape[1],"gdxtime", "True")
print(df_type_emission)


df_type_node = pd.read_excel(input, sheet_name="type_node")
print(df_type_node)
type(df_type_node)
df_type_node.insert(df_type_node.shape[1],"gdxtime", "True")
print(df_type_node)

df_type_tec = pd.read_excel(input, sheet_name="type_tec")
print(df_type_tec)
type(df_type_tec)
df_type_tec.insert(df_type_tec.shape[1],"gdxtime", "True")
print(df_type_tec)

df_type_year = pd.read_excel(input, sheet_name="type_year")
print(df_type_year)
type(df_type_year)
df_type_year.insert(df_type_year.shape[1],"gdxtime", "True")
print(df_type_year)


df_year = pd.read_excel(input, sheet_name="year")
print(df_year)
type(df_year)
df_year.insert(df_year.shape[1],"gdxtime", "True")
print(df_year)


#---- Parameters ----#
df_MERtoPPP = pd.read_excel(input, sheet_name="MERtoPPP")
cols = df_MERtoPPP.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_MERtoPPP = df_MERtoPPP[cols]
print(df_MERtoPPP)

df_abs_cost_activity_soft_lo = pd.read_excel(input, sheet_name="abs_cost_activity_soft_lo")
cols = df_abs_cost_activity_soft_lo.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_abs_cost_activity_soft_lo = df_abs_cost_activity_soft_lo[cols]
print(df_abs_cost_activity_soft_lo)


df_abs_cost_activity_soft_up = pd.read_excel(input, sheet_name="abs_cost_activity_soft_up")
cols = df_abs_cost_activity_soft_up.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_abs_cost_activity_soft_up = df_abs_cost_activity_soft_up[cols]
print(df_abs_cost_activity_soft_up)

df_aeei = pd.read_excel(input, sheet_name="aeei")
cols = df_aeei.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_aeei = df_aeei[cols]
print(df_aeei)

df_bound_activity_lo = pd.read_excel(input, sheet_name="bound_activity_lo")
cols = df_bound_activity_lo.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_bound_activity_lo = df_bound_activity_lo[cols]
print(df_bound_activity_lo)


df_bound_activity_up = pd.read_excel(input, sheet_name="bound_activity_up")
cols = df_bound_activity_up.columns.tolist()
print()
cols = cols[-1:] + cols[:-1]
df_bound_activity_up = df_bound_activity_up[cols]
print(df_bound_activity_up)

df_bound_extraction_up = pd.read_excel(input, sheet_name="bound_extraction_up")
cols = df_bound_extraction_up.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_bound_extraction_up = df_bound_extraction_up[cols]
print(df_bound_extraction_up)

df_bound_new_capacity_lo = pd.read_excel(input, sheet_name="bound_new_capacity_lo")
cols = df_bound_new_capacity_lo.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_bound_new_capacity_lo = df_bound_new_capacity_lo[cols]
print(df_bound_new_capacity_lo)

df_bound_new_capacity_up = pd.read_excel(input, sheet_name="bound_new_capacity_up")
cols = df_bound_new_capacity_up.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_bound_new_capacity_up = df_bound_new_capacity_up[cols]
print(df_bound_new_capacity_up)

df_bound_new_capacity_up = pd.read_excel(input, sheet_name="bound_new_capacity_up")
cols = df_bound_new_capacity_up.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_bound_new_capacity_up = df_bound_new_capacity_up[cols]
print(df_bound_new_capacity_up)

df_bound_total_capacity_lo = pd.read_excel(input, sheet_name="bound_total_capacity_lo")
cols = df_bound_total_capacity_lo.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_bound_total_capacity_lo = df_bound_total_capacity_lo[cols]
print(df_bound_total_capacity_lo)


df_bound_total_capacity_up = pd.read_excel(input, sheet_name="bound_total_capacity_up")
cols = df_bound_total_capacity_up.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_bound_total_capacity_up = df_bound_total_capacity_up[cols]
print(df_bound_total_capacity_up)

df_capacity_factor = pd.read_excel(input, sheet_name="capacity_factor")
cols = df_capacity_factor.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_capacity_factor = df_capacity_factor[cols]
print(df_capacity_factor)

df_commodity_stock = pd.read_excel(input, sheet_name="commodity_stock")
cols = df_commodity_stock.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_commodity_stock = df_commodity_stock[cols]
print(df_commodity_stock)

df_construction_time = pd.read_excel(input, sheet_name="construction_time")
cols = df_construction_time.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_construction_time = df_construction_time[cols]
print(df_construction_time)

df_cost_MESSAGE = pd.read_excel(input, sheet_name="cost_MESSAGE")
cols = df_cost_MESSAGE.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_cost_MESSAGE = df_cost_MESSAGE[cols]
print(df_cost_MESSAGE)

df_demand = pd.read_excel(input, sheet_name="demand")
cols = df_demand.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_demand = df_demand[cols]
print(df_demand)

df_demand_MESSAGE = pd.read_excel(input, sheet_name="demand_MESSAGE")
cols = df_demand_MESSAGE.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_demand_MESSAGE = df_demand_MESSAGE[cols]
print(df_demand_MESSAGE)

df_depr = pd.read_excel(input, sheet_name="depr")
cols = df_depr.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_depr = df_depr[cols]
print(df_depr)


df_drate = pd.read_excel(input, sheet_name="drate")
cols = df_drate.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_drate = df_drate[cols]
print(df_drate)


df_duration_period = pd.read_excel(input, sheet_name="duration_period")
cols = df_duration_period.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_duration_period = df_duration_period[cols]
print(df_duration_period)


df_duration_time = pd.read_excel(input, sheet_name="duration_time")
cols = df_duration_time.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_duration_time = df_duration_time[cols]
print(df_duration_time)


df_dynamic_land_up = pd.read_excel(input, sheet_name="dynamic_land_up")
cols = df_dynamic_land_up.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_dynamic_land_up = df_dynamic_land_up[cols]
print(df_dynamic_land_up)


df_emission_factor = pd.read_excel(input, sheet_name="emission_factor")
cols = df_emission_factor.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_emission_factor = df_emission_factor[cols]
print(df_emission_factor)

df_emission_scaling = pd.read_excel(input, sheet_name="emission_scaling")
cols = df_emission_scaling.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_emission_scaling = df_emission_scaling[cols]
print(df_emission_scaling)

df_esub = pd.read_excel(input, sheet_name="esub")
cols = df_esub.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_esub = df_esub[cols]
print(df_esub)


df_fix_cost = pd.read_excel(input, sheet_name="fix_cost")
cols = df_fix_cost.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_fix_cost = df_fix_cost[cols]
print(df_fix_cost)


df_gdp_calibrate = pd.read_excel(input, sheet_name="gdp_calibrate")
cols = df_gdp_calibrate.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_gdp_calibrate = df_gdp_calibrate[cols]
print(df_gdp_calibrate)


df_grow = pd.read_excel(input, sheet_name="grow")
cols = df_grow.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_grow = df_grow[cols]
print(df_grow)

df_growth_activity_lo = pd.read_excel(input, sheet_name="growth_activity_lo")
cols = df_growth_activity_lo.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_growth_activity_lo = df_growth_activity_lo[cols]
print(df_growth_activity_lo)

df_growth_activity_up = pd.read_excel(input, sheet_name="growth_activity_up")
cols = df_growth_activity_up.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_growth_activity_up = df_growth_activity_up[cols]
print(df_growth_activity_up)

df_growth_land_scen_lo = pd.read_excel(input, sheet_name="growth_land_scen_lo")
cols = df_growth_land_scen_lo.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_growth_land_scen_lo = df_growth_land_scen_lo[cols]
print(df_growth_land_scen_lo)

df_growth_land_up = pd.read_excel(input, sheet_name="growth_land_up")
cols = df_growth_land_up.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_growth_land_up = df_growth_land_up[cols]
print(df_growth_land_up)

df_growth_new_capacity_lo = pd.read_excel(input, sheet_name="growth_new_capacity_lo")
cols = df_growth_new_capacity_lo.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_growth_new_capacity_lo = df_growth_new_capacity_lo[cols]
print(df_growth_new_capacity_lo)


df_growth_new_capacity_up = pd.read_excel(input, sheet_name="growth_new_capacity_up")
cols = df_growth_new_capacity_up.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_growth_new_capacity_up = df_growth_new_capacity_up[cols]
print(df_growth_new_capacity_up)


df_historical_activity = pd.read_excel(input, sheet_name="historical_activity")
cols = df_historical_activity.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_historical_activity = df_historical_activity[cols]
print(df_historical_activity)


df_historical_extraction = pd.read_excel(input, sheet_name="historical_extraction")
cols = df_historical_extraction.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_historical_extraction = df_historical_extraction[cols]
print(df_historical_extraction)


df_historical_gdp = pd.read_excel(input, sheet_name="historical_gdp")
cols = df_historical_gdp.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_historical_gdp = df_historical_gdp[cols]
print(df_historical_gdp)

df_historical_land = pd.read_excel(input, sheet_name="historical_land")
cols = df_historical_land.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_historical_land = df_historical_land[cols]
print(df_historical_land)

df_historical_new_capacity = pd.read_excel(input, sheet_name="historical_new_capacity")
cols = df_historical_new_capacity.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_historical_new_capacity = df_historical_new_capacity[cols]
print(df_historical_new_capacity)


df_initial_activity_lo = pd.read_excel(input, sheet_name="initial_activity_lo")
cols = df_initial_activity_lo.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_initial_activity_lo = df_initial_activity_lo[cols]
print(df_initial_activity_lo)

df_initial_activity_up = pd.read_excel(input, sheet_name="initial_activity_up")
cols = df_initial_activity_up.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_initial_activity_up = df_initial_activity_up[cols]
print(df_initial_activity_up)


df_initial_new_capacity_lo = pd.read_excel(input, sheet_name="initial_new_capacity_lo")
cols = df_initial_new_capacity_lo.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_initial_new_capacity_lo = df_initial_new_capacity_lo[cols]
print(df_initial_new_capacity_lo)

df_initial_new_capacity_up = pd.read_excel(input, sheet_name="initial_new_capacity_up")
cols = df_initial_new_capacity_up.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_initial_new_capacity_up = df_initial_new_capacity_up[cols]
print(df_initial_new_capacity_up)

df_input = pd.read_excel(input, sheet_name="input")
cols = df_input.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_input = df_input[cols]
print(df_input)


df_interestrate = pd.read_excel(input, sheet_name="interestrate")
cols = df_interestrate.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_interestrate = df_interestrate[cols]
print(df_interestrate)


df_inv_cost = pd.read_excel(input, sheet_name="inv_cost")
cols = df_inv_cost.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_inv_cost = df_inv_cost[cols]
print(df_inv_cost)


df_kgdp = pd.read_excel(input, sheet_name="kgdp")
cols = df_kgdp.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_kgdp = df_kgdp[cols]
print(df_kgdp)


df_kpvs = pd.read_excel(input, sheet_name="kpvs")
cols = df_kpvs.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_kpvs = df_kpvs[cols]
print(df_kpvs)


df_lakl = pd.read_excel(input, sheet_name="lakl")
cols = df_lakl.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_lakl = df_lakl[cols]
print(df_lakl)


df_land_cost = pd.read_excel(input, sheet_name="land_cost")
cols = df_land_cost.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_land_cost = df_land_cost[cols]
print(df_land_cost)


df_land_emission = pd.read_excel(input, sheet_name="land_emission")
cols = df_land_emission.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_land_emission = df_land_emission[cols]
print(df_land_emission)


df_land_output = pd.read_excel(input, sheet_name="land_output")
cols = df_land_output.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_land_output = df_land_output[cols]
print(df_land_output)


df_land_output2 = pd.read_excel(input, sheet_name="land_output(2)")
cols = df_land_output2.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_land_output2 = df_land_output2[cols]
print(df_land_output2)


df_land_output3 = pd.read_excel(input, sheet_name="land_output(3)")
cols = df_land_output3.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_land_output3 = df_land_output3[cols]
print(df_land_output3)


df_land_use = pd.read_excel(input, sheet_name="land_use")
cols = df_land_use.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_land_use = df_land_use[cols]
print(df_land_use)


df_level_cost_activity_soft_lo = pd.read_excel(input, sheet_name="level_cost_activity_soft_lo")
cols = df_level_cost_activity_soft_lo.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_level_cost_activity_soft_lo = df_level_cost_activity_soft_lo[cols]
print(df_level_cost_activity_soft_lo)

df_level_cost_activity_soft_up = pd.read_excel(input, sheet_name="level_cost_activity_soft_up")
cols = df_level_cost_activity_soft_up.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_level_cost_activity_soft_up = df_level_cost_activity_soft_up[cols]
print(df_level_cost_activity_soft_up)

df_level_cost_new_capacity_soft_up = pd.read_excel(input, sheet_name="level_cost_new_capacity_soft_up")
cols = df_level_cost_new_capacity_soft_up.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_level_cost_new_capacity_soft_up = df_level_cost_new_capacity_soft_up[cols]
print(df_level_cost_new_capacity_soft_up)

df_lotol = pd.read_excel(input, sheet_name="lotol")
cols = df_lotol.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_lotol = df_lotol[cols]
print(df_lotol)


df_output = pd.read_excel(input, sheet_name="output")
cols = df_output.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_output = df_output[cols]
print(df_output)

df_prfconst = pd.read_excel(input, sheet_name="prfconst")
cols = df_prfconst.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_prfconst = df_prfconst[cols]
print(df_prfconst)

df_price_MESSAGE = pd.read_excel(input, sheet_name="price_MESSAGE")
cols = df_price_MESSAGE.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_price_MESSAGE = df_price_MESSAGE[cols]
print(df_price_MESSAGE)

df_ref_activity = pd.read_excel(input, sheet_name="ref_activity")
cols = df_ref_activity.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_ref_activity = df_ref_activity[cols]
print(df_ref_activity)


df_ref_extraction = pd.read_excel(input, sheet_name="ref_extraction")
cols = df_ref_extraction.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_ref_extraction = df_ref_extraction[cols]
print(df_ref_extraction)


df_ref_new_capacity = pd.read_excel(input, sheet_name="ref_new_capacity")
cols = df_ref_new_capacity.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_ref_new_capacity = df_ref_new_capacity[cols]
print(df_ref_new_capacity)


df_ref_relation = pd.read_excel(input, sheet_name="ref_relation")
cols = df_ref_relation.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_ref_relation = df_ref_relation[cols]
print(df_ref_relation)

df_relation_activity = pd.read_excel(input, sheet_name="relation_activity")
cols = df_relation_activity.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_relation_activity = df_relation_activity[cols]
print(df_relation_activity)

df_relation_lower = pd.read_excel(input, sheet_name="relation_lower")
cols = df_relation_lower.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_relation_lower = df_relation_lower[cols]
print(df_relation_lower)


df_relation_new_capacity = pd.read_excel(input, sheet_name="relation_new_capacity")
cols = df_relation_new_capacity.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_relation_new_capacity = df_relation_new_capacity[cols]
print(df_relation_new_capacity)


df_relation_total_capacity = pd.read_excel(input, sheet_name="relation_total_capacity")
cols = df_relation_total_capacity.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_relation_total_capacity = df_relation_total_capacity[cols]
print(df_relation_total_capacity)


# df_new_activity = pd.read_excel(input, sheet_name="new_activity")
# cols = df_new_activity.columns.tolist()
# cols = cols[-1:] + cols[:-1]
# df_new_activity = df_new_activity[cols]
# print(df_new_activity)


# df_total_capacity = pd.read_excel(input, sheet_name="total_capacity")
# cols = df_total_capacity.columns.tolist()
# cols = cols[-1:] + cols[:-1]
# df_total_capacity = df_total_capacity[cols]
# print(df_total_capacity)


df_relation_upper = pd.read_excel(input, sheet_name="relation_upper")
cols = df_relation_upper.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_relation_upper = df_relation_upper[cols]
print(df_relation_upper)


df_resource_cost = pd.read_excel(input, sheet_name="resource_cost")
cols = df_resource_cost.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_resource_cost = df_resource_cost[cols]
print(df_resource_cost)


df_resource_remaining = pd.read_excel(input, sheet_name="resource_remaining")
cols = df_resource_remaining.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_resource_remaining = df_resource_remaining[cols]
print(df_resource_remaining)


df_resource_volume = pd.read_excel(input, sheet_name="resource_volume")
cols = df_resource_volume.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_resource_volume = df_resource_volume[cols]
print(df_resource_volume)


df_soft_activity_lo = pd.read_excel(input, sheet_name="soft_activity_lo")
cols = df_soft_activity_lo.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_soft_activity_lo = df_soft_activity_lo[cols]
print(df_soft_activity_lo)


df_soft_activity_up = pd.read_excel(input, sheet_name="soft_activity_up")
cols = df_soft_activity_up.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_soft_activity_up = df_soft_activity_up[cols]
print(df_soft_activity_up)


df_soft_new_capacity_up = pd.read_excel(input, sheet_name="soft_new_capacity_up")
cols = df_soft_new_capacity_up.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_soft_new_capacity_up = df_soft_new_capacity_up[cols]
print(df_soft_new_capacity_up)

df_technical_lifetime = pd.read_excel(input, sheet_name="technical_lifetime")
cols = df_technical_lifetime.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_technical_lifetime = df_technical_lifetime[cols]
print(df_technical_lifetime)


df_var_cost = pd.read_excel(input, sheet_name="var_cost")
cols = df_var_cost.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_var_cost = df_var_cost[cols]
print(df_var_cost)

#---- set ----#
df_ix_type_mapping = pd.read_excel(input, sheet_name="ix_type_mapping")
print(df_ix_type_mapping)
type(df_ix_type_mapping)
df_ix_type_mapping.insert(df_ix_type_mapping.shape[1],"gdxtime", "True")
print(df_ix_type_mapping)

df_addon = pd.read_excel(input, sheet_name="addon")
print(df_addon)
type(df_addon)
df_addon.insert(df_addon.shape[1],"gdxtime", "True")
print(df_addon)


df_cat_addon = pd.read_excel(input, sheet_name="cat_addon")
print(df_cat_addon)
type(df_cat_addon)
df_cat_addon.insert(df_cat_addon.shape[1],"gdxtime", "True")
print(df_cat_addon)


df_cat_relation = pd.read_excel(input, sheet_name="cat_relation")
print(df_cat_relation)
type(df_cat_relation)
df_cat_relation.insert(df_cat_relation.shape[1],"gdxtime", "True")
print(df_cat_relation)

df_level_renewable = pd.read_excel(input, sheet_name="level_renewable")
print(df_level_renewable)
type(df_level_renewable)
df_level_renewable.insert(df_level_renewable.shape[1],"gdxtime", "True")
print(df_level_renewable)


df_level_storage = pd.read_excel(input, sheet_name="level_storage")
print(df_level_storage)
type(df_level_storage)
df_level_storage.insert(df_level_storage.shape[1],"gdxtime", "True")
print(df_level_storage)


df_map_shares_commodity_share = pd.read_excel(input, sheet_name="map_shares_commodity_share")
print(df_map_shares_commodity_share)
type(df_map_shares_commodity_share)
df_map_shares_commodity_share.insert(df_map_shares_commodity_share.shape[1],"gdxtime", "True")
print(df_map_shares_commodity_share)


df_map_shares_commodity_total = pd.read_excel(input, sheet_name="map_shares_commodity_total")
print(df_map_shares_commodity_total)
type(df_map_shares_commodity_total)
df_map_shares_commodity_total.insert(df_map_shares_commodity_total.shape[1],"gdxtime", "True")
print(df_map_shares_commodity_total)


df_map_tec_addon = pd.read_excel(input, sheet_name="map_tec_addon")
print(df_map_tec_addon)
type(df_map_tec_addon)
df_map_tec_addon.insert(df_map_tec_addon.shape[1],"gdxtime", "True")
print(df_map_tec_addon)


df_map_tec_storage = pd.read_excel(input, sheet_name="map_tec_storage")
print(df_map_tec_storage)
type(df_map_tec_storage)
df_map_tec_storage.insert(df_map_tec_storage.shape[1],"gdxtime", "True")
print(df_map_tec_storage)


df_shares = pd.read_excel(input, sheet_name="shares")
print(df_shares)
type(df_shares)
df_shares.insert(df_shares.shape[1],"gdxtime", "True")
print(df_shares)


df_storage_tec = pd.read_excel(input, sheet_name="storage_tec")
print(df_storage_tec)
type(df_storage_tec)
df_storage_tec.insert(df_storage_tec.shape[1],"gdxtime", "True")
print(df_storage_tec)


df_time_relative = pd.read_excel(input, sheet_name="time_relative")
print(df_time_relative)
type(df_time_relative)
df_time_relative.insert(df_time_relative.shape[1],"gdxtime", "True")
print(df_time_relative)


df_type_addon = pd.read_excel(input, sheet_name="type_addon")
print(df_type_addon)
type(df_type_addon)
df_type_addon.insert(df_type_addon.shape[1],"gdxtime", "True")
print(df_type_addon)


df_type_relation = pd.read_excel(input, sheet_name="type_relation")
print(df_type_relation)
type(df_type_relation)
df_type_relation.insert(df_type_relation.shape[1],"gdxtime", "True")
print(df_type_relation)


df_type_tec_land = pd.read_excel(input, sheet_name="type_tec_land")
print(df_type_tec_land)
type(df_type_tec_land)
df_type_tec_land.insert(df_type_tec_land.shape[1],"gdxtime", "True")
print(df_type_tec_land)


# gdx_balance_equality = df_balance_equality
gdx_Baseline = {'balance_equality':df_balance_equality,
                'cat_emission':df_cat_emission,
                'cat_node':df_cat_node,
                'cat_tec':df_cat_tec,
                'cat_year':df_cat_year,
                'commodity':df_commodity,
                'emission':df_emission,
                'grade':df_grade,
                'land_scenario':df_land_scenario,
                'land_type':df_land_type,
                'level':df_level,
                'level_resource':df_level_resource,
                'level_stocks':df_level_stocks,
                'lvl_spatial':df_lvl_spatial,
                'lvl_temporal':df_lvl_temporal,
                'map_node':df_map_node,
                'map_spatial_hierarchy':df_map_spatial_hierarchy,
                'map_temporal_hierarchy':df_map_temporal_hierarchy,
                'map_time':df_map_time,
                'mapping_macro_sector':df_mapping_macro_sector,
                'mode':df_mode,
                'node':df_node,
                'rating':df_rating,
                'relation':df_relation,
                'sector':df_sector,
                'technology':df_technology,
                'time':df_time,
                'type_emission':df_type_emission,
                'type_node':df_type_node,
                'type_tec':df_type_tec,
                'type_year':df_type_year,
                'year':df_year,
                'MERtoPPP':df_MERtoPPP,
                'abs_cost_activity_soft_lo':df_abs_cost_activity_soft_lo,
                'abs_cost_activity_soft_up':df_abs_cost_activity_soft_up,
                'aeei':df_aeei,
                'bound_activity_lo':df_bound_activity_lo,
                'bound_activity_up':df_bound_activity_up,
                'bound_extraction_up':df_bound_extraction_up,
                'bound_new_capacity_lo':df_bound_new_capacity_lo,
                'bound_new_capacity_up':df_bound_new_capacity_up,
                'bound_total_capacity_lo':df_bound_total_capacity_lo,
                'bound_total_capacity_up':df_bound_total_capacity_up,
                'capacity_factor':df_capacity_factor,
                'commodity_stock':df_commodity_stock,
                'construction_time':df_construction_time,
                'cost_MESSAGE':df_cost_MESSAGE,
                'demand':df_demand,
                'demand_MESSAGE':df_demand_MESSAGE,
                'depr':df_depr,
                'drate':df_drate,
                'duration_period':df_duration_period,
                'duration_time':df_duration_time,
                'dynamic_land_up':df_dynamic_land_up,
                'emission_factor':df_emission_factor,
                'emission_scaling':df_emission_scaling,
                'esub':df_esub,
                'fix_cost':df_fix_cost,
                'gdp_calibrate':df_gdp_calibrate,
                'grow':df_grow,
                'growth_activity_lo':df_growth_activity_lo,
                'growth_activity_up':df_growth_activity_up,
                'growth_land_scen_lo':df_growth_land_scen_lo,
                'growth_land_up':df_growth_land_up,
                'growth_new_capacity_lo':df_growth_new_capacity_lo,
                'growth_new_capacity_up':df_growth_new_capacity_up,
                'historical_activity':df_historical_activity,
                'historical_extraction':df_historical_extraction,
                'historical_gdp':df_historical_gdp,
                'historical_land':df_historical_land,
                'historical_new_capacity':df_historical_new_capacity,
                'initial_activity_lo':df_initial_activity_lo,
                'initial_activity_up':df_initial_activity_up,
                'initial_new_capacity_lo':df_initial_new_capacity_lo,
                'initial_new_capacity_up':df_initial_new_capacity_up,
                'input':df_input,
                'interestrate':df_interestrate,
                'inv_cost':df_inv_cost,
                'kgdp':df_kgdp,
                'kpvs':df_kpvs,
                'lakl':df_lakl,
                'land_cost':df_land_cost,
                'land_emission':df_land_emission,
                'land_output':df_land_output,
                'land_output_2':df_land_output2,
                'land_output_3':df_land_output3,
                'land_use':df_land_use,
                'level_cost_activity_soft_lo':df_level_cost_activity_soft_lo,
                'level_cost_activity_soft_up':df_level_cost_activity_soft_up,
                'level_cost_new_capacity_soft_up':df_level_cost_new_capacity_soft_up,
                'lotol':df_lotol,
                'output':df_output,
                'prfconst':df_prfconst,
                'price_MESSAGE':df_price_MESSAGE,
                'ref_activity':df_ref_activity,
                'ref_extraction':df_ref_extraction,
                'ref_new_capacity':df_ref_new_capacity,
                'ref_relation':df_ref_relation,
                'relation_activity':df_relation_activity,
                'relation_lower':df_relation_lower,
                'relation_new_capacity':df_relation_new_capacity,
                'relation_total_capacity':df_relation_total_capacity,
                'relation_upper':df_relation_upper,
                'resource_cost':df_resource_cost,
                'resource_remaining':df_resource_remaining,
                'resource_volume':df_resource_volume,
                'soft_activity_lo':df_soft_activity_lo,
                'soft_activity_up':df_soft_activity_up,
                'soft_new_capacity_up':df_soft_new_capacity_up,
                'technical_lifetime':df_technical_lifetime,
                'var_cost':df_var_cost,
                'ix_type_mapping':df_ix_type_mapping,
                'addon':df_addon,
                'cat_addon':df_cat_addon,
                'cat_relation':df_cat_relation,
                'level_renewable':df_level_renewable,
                'level_storage':df_level_storage,
                'map_shares_commodity_share':df_map_shares_commodity_share,
                'map_shares_commodity_total':df_map_shares_commodity_total,
                'map_tec_addon':df_map_tec_addon,
                'map_tec_storage':df_map_tec_storage,
                'shares':df_shares,
                'storage_tec':df_storage_tec,
                'time_relative':df_time_relative,
                'type_addon':df_type_addon,
                'type_relation':df_type_relation,
                'type_tec_land':df_type_tec_land}

gdx_file = "../MsgData_MESSAGEix-GLOBIOM 1.1-R12_baseline_DEFAULT.gdx"
gdx = gdxpds.to_gdx(gdx_Baseline, gdx_file)

# xlsx = openpyxl.load_workbook(input)
# symbol_name1 = xlsx.get_sheet_names() # deprecated feature
# print(symbol_name1)
# type(symbol_name1)
# symbol_name11=pd.DataFrame(symbol_name1)
# symbol_name11.to_excel("names.xlsx")

