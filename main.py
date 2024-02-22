#https://www.analyticsvidhya.com/blog/2020/09/precision-recall-machine-learning/


import os
from csv_importer import ProcessCSV
from llm_communicate import LLM_Communicator
from openai import OpenAI
import os

from rimay_verification import Paska_tool

client = None

    
def multiple_times():
    ask_llm_to_convert()
    show_verification_question()
    

    
    
def main():

    paska_tool = Paska_tool()
    llm_communicator = LLM_Communicator()
    llm_communicator.setup_llm()
    #all gherkin data.
    csv_importer = ProcessCSV() #GherkinData

    #when done, write to file for RimayData.

    setup_llm()
    multiple_times()
    show_results()

if __name__ == "__main__":
    main()