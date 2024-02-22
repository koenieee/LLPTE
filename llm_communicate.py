from openai import OpenAI
import os

from prompt_techniques import LLM_prompt_technique


class LLM_Communicator():
    def __init__(self) -> None:
        pass


    def setup_llm():
        global client
        client = OpenAI(
            # This is the default and can be omitted
            api_key="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",
        )



    def ask_llm_to_convert(question: LLM_prompt_technique):
        pass
        global client
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            model="gpt-3.5-turbo",
        )
