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
        return f"{self.question}. Use the following Gherkin acceptance criteria input data : {self.input_obj}"

    def __repr__(self) -> str:
        return f"================\nQuestion: {self.question}\nInput_data: {self.input_obj}\n================"
    
class LLM_few_shot_learning(LLM_prompt_technique, LLM_prompt_data):
    def __init__(self, input: LLM_prompt_data):
        prompt_method = """
        The following syntax structure is called Rimay, this is a CNL (Controlled Natural Language)

        WHEN_STRUCTURE : When TRIGGER
        ACTOR = example: System A
        MODAL_VERB = example: should, can, could, might, will
        SYSTEM_RESPONSE = SYSTEM_RESPONSE_EXPRESSION | RESPONSE_BLOCK_ITEMIZED SYSTEM_RESPONSE_EXPRESSION: ATOMIC_SYSTEM_RESPONSE ((,|, and|, or|and|or)? ATOMIC_SYSTEM_RESPONSE)* ATOMIC_SYSTEM_RESPONSE: ACTION_PHRASE (every TEXT )? RESPONSE_BLOCK_ITEMIZED: do the following actions (in sequence)? : BULLET ATOMIC_SYSTEM_RESPONSE ((,|, and|, or|and|or)? BULLET ATOMIC_SYSTEM_RESPONSE)*

        ACTOR, MODAL_VERB and a SYSTEM_RESPONSE is mandatory in all Rimay requirements.

        Can you convert the following Gherkin input into the Rimay CNL output?
        """
        super().__init__( input, prompt_method)

    
class LLM_chain_of_thought(LLM_prompt_technique, LLM_prompt_data):
    def __init__(self, input: LLM_prompt_data):
        prompt_method = """
        Learn from the following example, the output information for the CNL Rimay is: 
        This part is the start of the example you have to learn from:

        The input information is as follows: 

        Acceptance Criteria 1 in Gherkin, input:
        Gherkin:
        Scenario: Create an Order
        Given an Order of type Subscription_Order does not exist in OI of type Order_Issuer 
        When OI Create Order, 
        Then Order exists in OI 
        And the property settlement_method of Order is equal to FOP


        Rimay output 1:
        When the Order_Issuer (OI ) executes Create a Subscription_Order, if the Order does not exist, then the Order is created and its settlement_method is set to FOP.

        Rimay uses the following structure:
        When the? Actor <Action> (every "Frequency")? ,|then the? Actor must <Action> (every "Text")?.

        Ending for example


        Translate the following input acceptance criteria Gherkin, according to the example above, to Rimay:


        """
        super().__init__(input, prompt_method)


class LLM_role_play(LLM_prompt_technique, LLM_prompt_data) : 
    def __init__(self, input: LLM_prompt_data):
        prompt_method = """
        Behave like a person who writes the Controlled Natural Language (CNL) Rimay.
        Rimay is a language that is defined in different components. 
        For now we only highlight the following components:

        Mandatory:
        ACTOR = example: System A
        MODAL_VERB = example: should, can, could, might, will
        SYSTEM_RESPONSE = SYSTEM_RESPONSE_EXPRESSION | RESPONSE_BLOCK_ITEMIZED 
        SYSTEM_RESPONSE_EXPRESSION: ATOMIC_SYSTEM_RESPONSE ((,|, and|, or|and|or)? ATOMIC_SYSTEM_RESPONSE)* ATOMIC_SYSTEM_RESPONSE: ACTION_PHRASE (every TEXT )? RESPONSE_BLOCK_ITEMIZED: do the following actions (in sequence)? : BULLET ATOMIC_SYSTEM_RESPONSE ((,|, and|, or|and|or)? BULLET ATOMIC_SYSTEM_RESPONSE)*
        Optional:
        WHEN_STRUCTURE : When TRIGGER


        ACTOR, MODAL_VERB and a SYSTEM_RESPONSE is mandatory in all Rimay requirements.

        Rimay: WHEN_STRUCTURE  ACTOR   MODAL_VERB     SYSTEM_RESPONSE

        Now I want you to answer as the person who writes Rimay to translate this acceptance criteria into Rimay

        """
        super().__init__(input, prompt_method)




