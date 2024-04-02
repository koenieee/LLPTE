#https://www.analyticsvidhya.com/blog/2020/09/precision-recall-machine-learning/


import os
from data_importer import GherkinData
from html_gui import setup_ui
from nicegui import ui


from standalone_rimay import results, start_gherkin_translation


import sys


client = None


# Read all gherkin data
# Score systeem.
# Log all outputs
# improve prompt techniques.
n = len(sys.argv)
print("Total arguments passed:", n)
    
# all gherkin data.

# Gherkin acceptance criteria inspriation comes from:
# Open_Source_Projects_GitHub_US_AC_Analysis.xlsx
# https://zenodo.org/records/6460854
gherkin_acceptance_criteria = GherkinData() #GherkinData
all_acceptance_criteria = gherkin_acceptance_criteria.get_all_acceptance_criteria()


gui = str(sys.argv[1])


if gui == "standalone":
    range_start = int(sys.argv[2]) or 0
    range_end = int(sys.argv[3]) or 20
    techniek = sys.argv[4] or "Few-shot-learning"

    print(gherkin_acceptance_criteria)
    print(len(all_acceptance_criteria))
# Standalone?
    for scenario in all_acceptance_criteria[range_start:range_end]:
        scenario_name = scenario["scenario_name"]
        content_acceptance_criteria = scenario["simplified"]

        print(scenario_name+"\n")
        start_gherkin_translation(scenario_name, content_acceptance_criteria, techniek)
elif gui == "results":
    techniek = str(sys.argv[2]) or "Few-shot-learning"
    data_directory = f"output_dataset/{techniek}/"
    results(data_directory)
else:
    setup_ui()
    ui.run()


