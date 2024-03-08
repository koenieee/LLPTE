
import os

import openai
openai.api_key = "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"

from prompt_techniques import LLM_prompt_technique


#https://github.com/zauberzeug/nicegui/blob/main/examples/progress/main.py

class LLM_Communicator():

    def __init__(self) -> None:
        self.client = None


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

        return anwer_content
