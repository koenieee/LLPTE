from prompt_techniques import LLM_prompt_technique
from datetime import datetime
import uuid

class ResearchLogger():
    
    def __init__(self, prefix_name) -> None:
        self.log_directory = "prompt_logging/"
        self.timestamp = datetime.now().strftime("%m_%d_%Y__%H:%M:%S")
        self.prefix = prefix_name
        self.log_file = f"{self.log_directory}/{self.prefix}_{self.timestamp}.md"
        self.file_contents = ""
        self.write_header()

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


    def append_result(self, result):
        self.file_contents += f"\n{result}\n"
        self.write_to_file()

