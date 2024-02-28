class LLM_prompt_data():
    def __init__(self) -> None:
        pass


    def precondition_data(self): #todo, for gherkin i guess
        pass 

    def postcondition_data(self): #todo for rimay i guess
        pass



class LLM_prompt_technique:
    def __init__(self, quest):
        self.question = quest
        pass

    def __str__(self) -> str:
        return f"Tell me the story of LLM prompt technique: {self.question}"

    def __repr__(self) -> str:
        return f"================\n{self.question}\n================"
    
class LLM_few_shot_learning(LLM_prompt_technique, LLM_prompt_data):
    def __init__(self):
        super().__init__(" with few short learning")

    
class LLM_chain_of_thought(LLM_prompt_technique, LLM_prompt_data):
    def __init__(self):
        super().__init__(" with chain of thought learning")


class LLM_role_play(LLM_prompt_technique, LLM_prompt_data) : 
    def __init__(self):
        super().__init__(" with role play")




