


import os
import re
from logger import ResearchLogger
from rimay_verification import Paska_tool, RimayDSL
from wrapper_calls import ask_different_prompts
from nicegui import ui
from random import random


#['Few-shot learning', 'Chain-of-thought', 'Role play']

start_rimay_actors = """Actors: actor SystemA, actor SystemB, actor SystemC, actor UserX, actor UserA, actor UserC
Classes: class Instruction := description record, class Y
"""


def convert_single_gherkin_to_rimay(scenario_name: str, input_text:str, translation_type: str, incorrect, temperature):
    current_logger = ResearchLogger(translation_type, temperature, scenario_name) #Vervalt bij nieuwe logger.

    pre_content = f"""
# Scenario Name {scenario_name}

    """

    pre_content = f"""
## Gherkin Input
```
{input_text.strip()}
```
    """
    current_logger.append_result(pre_content)
    response = ask_different_prompts(input_text.strip(), translation_type, current_logger, incorrect, temperature)
    researcher_score(input_text, response, current_logger)
    rimay_check(response, current_logger)

def researcher_score(inp, output, current_logger: ResearchLogger):
    print("//////////////////////////////////")
    print("Input Gherkin: ")
    print(inp)
    print("=================")
    print("output Rimay: ")
    print(output)
    print("=================")
    print("Score for Rimay?")
    print("[0] = Failure")
    print("[1] = Mediocre")
    print("[2] = Sufficient")
    print("[3] = Good")
    print('\a') #bell sound.
    score_choice = int(input('Score: [0..3]: \n'))
    score_options = [-10, -5, +10, +15]
    
    print("//////////////////////////////////")
    
    current_logger.custom_researcher_score(score_options[score_choice])


def rimay_check(rimay_text, current_logger: ResearchLogger):
    dsl = RimayDSL()

    dsl.check_rimay_comf_dsl(start_rimay_actors + rimay_text)
    dsl.write_log_output(current_logger)

    paska_tool = Paska_tool()

    paska_tool.check_rimay_requirement(rimay_text.strip().replace("\n",""))
    paska_tool.write_log_output(current_logger)

    current_logger.generate_final_score()
    current_logger = None




def start_gherkin_translation(scenario_name: str, acceptance_criteria: str, techniek, llmtemp):
    convert_single_gherkin_to_rimay(scenario_name, acceptance_criteria, techniek, False, llmtemp)
    convert_single_gherkin_to_rimay(scenario_name + "_Incorrect_", acceptance_criteria, techniek, True, llmtemp)

    # convert_single_gherkin_to_rimay(scenario_name, acceptance_criteria, "Chain-of-thought")
    # convert_single_gherkin_to_rimay(scenario_name, acceptance_criteria, "Role play")



def results(path):
    scenarios_TP = []
    scenarios_TN = []
    data_values_TP = []
    data_values_TN = []
    lst = os.listdir(path)
    lst.sort()


    for x in lst:
        if x.endswith(".md"):
            all_data = x.split('__')
            print(all_data)
            scenario_num = re.findall(r'\d+', all_data[0])[0]
            date = all_data[1]
            time = all_data[2]
            score = re.findall(r'\d+', all_data[3])[0]
            if "_Incorrect_" in x:

                scenarios_TN.append(f"Generated Rimay {scenario_num}")
                data_values_TN.append(int(score))

            else:
                scenarios_TP.append(f"Generated Rimay {scenario_num}")
                data_values_TP.append(int(score))


            

            # Prints only text file present in My Folder
            print(x)
            # print(scenario_num)
            # print(date)
            # print(score)

    # print(scenarios)
    # print(data_values)
    print(scenarios_TP)
    print(data_values_TP)
    print(data_values_TN)


    chart = ui.highchart({
    'title': False,
    'chart': {'type': 'bar'},
    'xAxis': {'categories': scenarios_TP},
    'series': [
        {'name': path.replace("output_dataset/", "").replace("/", "").replace("_", " ") + " TP", 'data': data_values_TP},
        {'name': path.replace("output_dataset/", "").replace("/", "").replace("_", " ")  + " TN", 'data': data_values_TN},

        # {'name': 'Few-Shot-learning Incorrect (TN)', 'data': [12, 13, 14]},

        # {'name': 'Chain-of-thought', 'data': [12, 56, 72]},
        # {'name': 'Role-Play', 'data': [57, 44, 82]},


        ],
    }).classes('w-full h-200')

    def update():
        chart.options['series'][0]['data'][0] = random()
        chart.update()

    ui.button('Update', on_click=update)

    ui.run()
