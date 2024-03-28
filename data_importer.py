import re
from prompt_techniques import LLM_prompt_data
import csv
import xml.etree.ElementTree as ET
import json



class ProcessTextFile():
    def __init__(self) -> None:
        pass

    def _load_csv_file(self, filename, items):

        all_lines = []
        all_lines.append(items)
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                    continue
                row_item = {}
                for item in items:
                    row_item[item] = row[items[item]]

                all_lines.append(row_item)
                line_count += 1
            print(f'Processed {line_count} lines.')
        return all_lines
    
    def _load_xml_file(self, filename):

        root = ET.parse(filename)
        all_dicts = []
        parsed_dict = dict()
        for child in root.iter():
            if child.text.strip():
                parsed_dict[child.tag] = re.sub(' +', ' ', child.text.strip()).replace('\n ','\n')
            if len(parsed_dict) > 3:
                all_dicts.append(parsed_dict)
                parsed_dict = dict()


        return all_dicts

    
    def save(self):
        Exception("not implemented")
        pass


    def prepare_for_proces():
        pass



class GherkinData(ProcessTextFile, LLM_prompt_data):
    def __init__(self) -> None:
        super().__init__()
        self.gherkin_list = self.load()

    def load(self):
        return super()._load_xml_file("input_dataset/input_dataset.xml")
    
    #save not implemented

    def get_all_acceptance_criteria(self):
        return self.gherkin_list

    def __str__(self):
        make_str = ""
        for scenario in self.gherkin_list:
            scenario_name = scenario["scenario_name"]
            content_acceptance_criteria = scenario["simplified"]
            manual = scenario["manual_translation"]


            make_str += "========================\n"
            make_str += scenario_name+"\n"
            make_str += "////////////////////////\n"
            make_str += content_acceptance_criteria+"\n"
            make_str += "========================\n"
        return make_str

    def __repr__(self) -> str:

        return self.__str__()



class RimayData(ProcessTextFile, LLM_prompt_data):
    def __init__(self) -> None:
        super().__init__()
    #load not implemented
    

    def load(self):
        items = {"Req Segment": 2, "Rimay Pattern":12, "Rimay Structure":13,  "Non-atomic requirement": 3, "Incomplete requirement": 4, "Incorrect order requirement": 5, "Coordination ambiguity": 6, "Not requirement": 7, "Incomplete condition": 8, "Incomplete system response":9, "Passive voice":10, "Not precise verb":11}

        return super()._load_csv_file("./generated_data/output_smells/generated_rimay.csv.csv.csv", items)
    

    def save(self):
        return super().save()

    def prepare_for_proces(self):
        return "Rimay data needs to be stripped and processed."     