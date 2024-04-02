import os
from prompt_techniques import LLM_prompt_technique
from datetime import datetime
import uuid

class ResearchLogger():
    
    def __init__(self, prefix_name, scenario_name: str = "") -> None:
        self.log_directory = "output_dataset/"
        self.timestamp = datetime.now().strftime("%m_%d_%Y__%H:%M:%S")
        self.prefix = prefix_name
        self.scenario = scenario_name
        self.log_file = f"{self.log_directory}/{self.prefix}/{self.scenario}__{self.timestamp}.md"
        self.file_contents = ""
        self.write_header()
        self.final_score = 0
        self.number_of_scores = 0
        self.researcher_score = 0

    def write_header(self):
        self.file_contents += f"""

# LLM Experiment Information
* Prefix:   {self.prefix}
* Datetime: {self.timestamp}
* UniqueID: {uuid.uuid4()}
* Scenario name: {self.scenario}

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

    def custom_researcher_score(self, score):
        self.researcher_score = score
        self.file_contents = f"""
### Researcher score
Researcher_score = {score}


"""


        self.write_to_file()


    def generate_final_score(self):
        if self.researcher_score > 0 : 

            this_score = min(100, ( self.final_score / self.number_of_scores ) + self.researcher_score)
        else:
            this_score = min(100, ( self.final_score / self.number_of_scores ) - abs(self.researcher_score))

        print("FINAL score")
        print(self.researcher_score )
        print(self.final_score)
        print(self.number_of_scores)
        print(self.researcher_score)
        print("Final:")
        print(this_score)

        self.file_contents = f"""
### Final Score
Final_score = {this_score}

Progressbar: ![{this_score}%](https://progress-bar.dev/{this_score})

"""


        self.write_to_file()

        # Absolute path of a file
        old_name =  self.log_file 
        new_name = f"{self.log_directory}/{self.prefix}/{self.scenario}__{self.timestamp}__{this_score}_score.md"

        # Renaming the file
        os.rename(old_name, new_name)


    def append_result(self, result):
        self.file_contents += f"\n{result}\n"
        self.write_to_file()

