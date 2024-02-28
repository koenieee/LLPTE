import time
from openai import OpenAI

import os

from prompt_techniques import LLM_prompt_technique


#https://github.com/zauberzeug/nicegui/blob/main/examples/progress/main.py

class LLM_Communicator():

    def __init__(self) -> None:
        self.client = None
        self.setup_llm()


    def setup_llm(self):
        self.client = OpenAI(
            # This is the default and can be omitted
            api_key="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",
        )


    def ask_llm_to_convert(self, question: LLM_prompt_technique):
        print(repr(question))
        # time.sleep(3)
        # return "baaall"

        #  {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        #     {"role": "user", "content": "Who won the world series in 2020?"}
        # https://platform.openai.com/docs/guides/prompt-engineering
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    
                    "role": "user",
                    "content": str(question),
                }
            ],
            model="gpt-3.5-turbo",
        )
        answer = chat_completion.choices[0].message.content
        return answer
