from prompt_techniques import LLM_prompt_technique


class ResearchLogger():
    
    def __init__(self) -> None:
        self.log_file_prompting = "./logfile_llm_prompt.md"

    def write_header():
        #Timestamp
        #Browserinstance name
        #

    def write_to_file(self, input_prompt: LLM_prompt_technique, output_result: str):
        f = open(self.log_file_prompting, "a")
        f.write("\n")
        
        f.write(f"### Input prompt, technique: {input_prompt.name()}\n")
        f.write("\n```\n")
        f.write(str(input_prompt))
        f.write("\n```\n")
        f.write("### Output result \n")
        f.write(output_result)
        
        f.write("\n")
        f.close()    

    def start_new_translation():
        pass

    def append_dsl_result(result):
        #check if current translation is active
        pass

    def append_paska_result(result):
        #check if current translation is active
        pass

