import threading
from llm_communicate import LLM_Communicator
from openai import OpenAI
import os
from prompt_techniques import LLM_chain_of_thought, LLM_few_shot_learning, LLM_role_play

def ask_different_prompts() -> str:
    llm_communicator = LLM_Communicator()
    fsl_prompt = LLM_few_shot_learning()
    cot_prompt = LLM_chain_of_thought()
    rp_prompt = LLM_role_play()
    result = llm_communicator.ask_llm_to_convert(fsl_prompt)
    result = result + llm_communicator.ask_llm_to_convert(cot_prompt)
    result = result + llm_communicator.ask_llm_to_convert(rp_prompt)
    # finished_function(result)
    return result


