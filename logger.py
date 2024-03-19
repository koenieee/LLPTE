import os
from prompt_techniques import LLM_prompt_technique
from datetime import datetime
import uuid

class ResearchLogger():
    
    def __init__(self, prefix_name) -> None:
        self.log_directory = "output_dataset/"
        self.timestamp = datetime.now().strftime("%m_%d_%Y__%H:%M:%S")
        self.prefix = prefix_name
        self.log_file = f"{self.log_directory}/{self.prefix}/{self.prefix}_{self.timestamp}.md"
        self.file_contents = ""
        self.write_header()
        self.final_score = 0
        self.number_of_scores = 0

    def write_header(self):
        self.file_contents += f"""

# LLM Experiment Information
* Prefix:   {self.prefix}
* Datetime: {self.timestamp}
* UniqueID: {uuid.uuid4()}

        """
        self.write_to_file()

    def write_to_file(self):
        f = open(self.log_file, "a")
        f.write(self.file_contents)
        self.file_contents = ""
        f.close()    

    def append_score(self, score):
        self.final_score += score
        self.number_of_scores += 1

    def generate_final_score(self):
        this_score = self.final_score / self.number_of_scores
        self.file_contents = f"""
### Final Score
Final_score = {this_score}
"""


        self.write_to_file()

        # Absolute path of a file
        old_name =  self.log_file 
        new_name = f"{self.log_directory}/{self.prefix}/{self.prefix}_{this_score}_score_{self.timestamp}.md"

        # Renaming the file
        os.rename(old_name, new_name)


    def append_result(self, result):
        self.file_contents += f"\n{result}\n"
        self.write_to_file()

