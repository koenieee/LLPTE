
import os

import openai
openai.api_key = "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"

from prompt_techniques import LLM_prompt_technique


#https://github.com/zauberzeug/nicegui/blob/main/examples/progress/main.py

class LLM_Communicator():

    def __init__(self) -> None:
        self.client = None
        self.log_file_prompting = "./logfile_llm_prompt.md"

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



    def ask_llm_to_convert(self, question: LLM_prompt_technique):
        print(str(question))

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", # engine = "deployment_name".
            temperature=0.2,
            messages=[
                
                {"role": "user", "content": str(question)},
                
            ]
        )
        anwer_content = response['choices'][0]['message']['content']

        self.write_to_file(question, anwer_content)
        return anwer_content
