#https://www.analyticsvidhya.com/blog/2020/09/precision-recall-machine-learning/


import os
from data_importer import GherkinData, RimayData
from html_gui import setup_ui
from nicegui import ui


from rimay_verification import Paska_tool

client = None

    

# write csv file
# generate parsing trees
#conda activate smell-detector
# python /home/koebuntu/LLPTE/existing_research/paska/source/get-parsing-trees/get_cparsingtrees.py "/home/koebuntu/LLPTE/existing_research/paska/example/input_koen/" "/home/koebuntu/LLPTE/existing_research/paska/example/output_koen/"
# check smell with paska
#java -jar smell_detector.jar /home/koebuntu/LLPTE/existing_research/paska/example/output_koen/ /home/koebuntu/LLPTE/existing_research/paska/example/smells_koen/ /home/koebuntu/LLPTE/existing_research/paska/example/english-left3words-distsim.tagger 


#/home/koebuntu/LLPTE/existing_research/paska/example/smells_koen/


# paska_tool.check_rimay_requirement("When an order cancellation message is received from the System-A then Reason must be displayed in the Sytem-B GUI field 'Reason of Cancellation'.")
# paska_tool.check_rimay_requirement("When the System-A receives a rejection message from System-B, Then it must transform it to the corresponding XML  message type and sent it to the System-C.")

#all gherkin data.
csv_importer = GherkinData() #GherkinData
all_acceptance_criteria = csv_importer.load()

for scenario in all_acceptance_criteria:
    print(scenario["scenario_name"])
    print(scenario["content"])
    print("=================")

setup_ui()
ui.run()

# rimay = RimayData()
# print(rimay.load())

