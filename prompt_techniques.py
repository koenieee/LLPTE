class LLM_prompt_data():
    def __init__(self, text: str) -> None:
        self.text = text


    def __str__(self) -> str:
        return self.text

    def precondition_data(self): #todo, for gherkin i guess
        pass 

    def postcondition_data(self): #todo for rimay i guess
        pass



class LLM_prompt_technique:
    def __init__(self, input_obj:LLM_prompt_data, quest: str):
        self.input_obj = input_obj
        self.question = quest
        pass

    def __str__(self) -> str:
        return f"Tell me the story of LLM prompt technique: {self.question}. Use the following input data: {self.input_obj}"

    def __repr__(self) -> str:
        return f"================\nQuestion: {self.question}\nInput_data: {self.input_obj}\n================"
    
class LLM_few_shot_learning(LLM_prompt_technique, LLM_prompt_data):
    def __init__(self, input: LLM_prompt_data):
        super().__init__( input, " with few short learning")

    
class LLM_chain_of_thought(LLM_prompt_technique, LLM_prompt_data):
    def __init__(self, input: LLM_prompt_data):
        super().__init__(input, " with chain of thought learning")


class LLM_role_play(LLM_prompt_technique, LLM_prompt_data) : 
    def __init__(self, input: LLM_prompt_data):
        super().__init__(input, " with role play")




