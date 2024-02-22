class ProcessCSV():
    def __init__(self) -> None:
        pass

    def load(self):
        Exception("not implemented")
        pass

    
    def save(self):
        Exception("not implemented")
        pass


    def prepare_for_proces():
        pass

class LLM_prompt_data():
    def __init__(self) -> None:
        pass


    def precondition_data():
        pass 

    def postcondition_data():
        pass



class GherkinData(ProcessCSV, LLM_prompt_data):
    def __init__(self) -> None:
        super().__init__()

    def load(self):
        return super().load()
    
    #save not implemented



class RimayData(ProcessCSV, LLM_prompt_data):
    def __init__(self) -> None:
        super().__init__()
    #load not implemented
    
    def save(self):
        return super().save()

    def prepare_for_proces(self):
        return "Rimay data needs to be stripped and processed."