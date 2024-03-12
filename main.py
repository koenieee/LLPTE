#https://www.analyticsvidhya.com/blog/2020/09/precision-recall-machine-learning/


import os
from data_importer import GherkinData, RimayData
from html_gui import setup_ui
from nicegui import ui


from rimay_verification import Paska_tool, RimayDSL

client = None

    
#all gherkin data.
csv_importer = GherkinData() #GherkinData
all_acceptance_criteria = csv_importer.load()

for scenario in all_acceptance_criteria:
    print(scenario["scenario_name"])
    print(scenario["content"])
    print("=================")

setup_ui()
ui.run()


