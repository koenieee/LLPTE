from prompt_techniques import LLM_prompt_data
import csv
import xml.etree.ElementTree as ET
import json



class ProcessTextFile():
    def __init__(self) -> None:
        pass

    # def load_csv(self, filename, col_value):
    #     all_lines = []
    #     with open(filename, mode='r') as csv_file:
    #         csv_reader = csv.reader(csv_file, delimiter=';')
    #         line_count = 0
    #         for row in csv_reader:
    #             if line_count == 0:
    #                 print(f'Column names are {", ".join(row)}')
    #                 line_count += 1
    #             all_lines.append(row[0])
    #             line_count += 1
    #         print(f'Processed {line_count} lines.')
    #     return all_lines
    
    def load_xml_file(self, filename, col_value):

        root = ET.parse(filename)
        all_dicts = []
        parsed_dict = dict()
        for child in root.iter():
            if child.text.strip():
                parsed_dict[child.tag] = child.text
            if len(parsed_dict) > 1:
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

    def load(self):
        return super().load_xml_file("input_dataset.xml", "acceptance_criteria")
    
    #save not implemented



class RimayData(ProcessTextFile, LLM_prompt_data):
    def __init__(self) -> None:
        super().__init__()
    #load not implemented
    
    def save(self):
        return super().save()

    def prepare_for_proces(self):
        return "Rimay data needs to be stripped and processed."     