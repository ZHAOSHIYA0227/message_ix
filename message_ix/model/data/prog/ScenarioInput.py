import ixmp 
import message_ix
import matplotlib.pyplot as plt
# import xlrd
# import openpyxl
# import gdxpds
import pandas as pd
import os
import requests
import base64

# os.environ['myUsername'] = 'desktop-fgglssd/taiki'
# os.environ['myPassword'] = 'taiki'

# USER = os.getenv('myUsername')
# print(USER)
# PASSWORD = os.environ.get('myPassword')
# print(PASSWORD)
# token = base64.b64encode(f"{USER}:{PASSWORD}")
# r=requests.get(auth_url, headers={"Authorization": f"Basic {token}"})

mp = ixmp.Platform()

# input = "../xlsx/MESSAGEix-GLOBIOM 1.1-R12_baseline_DEFAULT.xlsx"
input = "data/xlsx/MESSAGEix-GLOBIOM 1.1-R12_baseline_DEFAULT.xlsx"

Model = "MESSAGE_DEFAULT"

bau = message_ix.Scenario(mp, model=Model, scenario="baseline_xlsx", version="new")

# scenario = message_ix.Scenario(
#     mp, model="Westeros Electrified", scenario="baseline_xlsx", version="new"
# )

bau.read_excel(input, add_units=True, init_items=True)
bau.solve()

scen = base.clone(
    Model,
    "flexible_generation",
    "illustration of flexible-generation formulation",
    keep_solution=False,
)
scen.check_out()

scen.solve()