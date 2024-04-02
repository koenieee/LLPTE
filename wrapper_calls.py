from llm_communicate import LLM_Communicator
from prompt_techniques import LLM_chain_of_thought, LLM_few_shot_learning, LLM_prompt_data, LLM_role_play
from logger import ResearchLogger 


def ask_different_prompts(input_text: str, prompt_tech: str, log:ResearchLogger, incorrect: bool = False) -> str:
    prompt_data = LLM_prompt_data(input_text)
    llm_communicator = LLM_Communicator()
    fsl_prompt = LLM_few_shot_learning(prompt_data, incorrect)
    cot_prompt = LLM_chain_of_thought(prompt_data, incorrect)
    rp_prompt = LLM_role_play(prompt_data, incorrect)
    result = ""
    if prompt_tech.strip() == "Few-shot-learning": #['Few-shot learning', 'Chain-of-thought', 'Role play']
        result = llm_communicator.ask_llm_to_convert(fsl_prompt)
    elif prompt_tech.strip() == "Chain-of-thought":
        result = llm_communicator.ask_llm_to_convert(cot_prompt)
    else: #Role play
        result = llm_communicator.ask_llm_to_convert(rp_prompt)

    llm_communicator.write_log_output(log)
    
    return result