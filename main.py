#https://www.analyticsvidhya.com/blog/2020/09/precision-recall-machine-learning/


import os
from csv_importer import ProcessCSV
from html_gui import setup_ui


from rimay_verification import Paska_tool
from nicegui import ui

client = None

    


paska_tool = Paska_tool()

#all gherkin data.
csv_importer = ProcessCSV() #GherkinData


setup_ui()
ui.run()



#when done, write to file for RimayData.

# setup_llm()
# multiple_times()
# show_results()
