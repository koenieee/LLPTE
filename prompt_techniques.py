class LLM_prompt_data():
    def __init__(self, text: str) -> None:
        self.text = text


    def __str__(self) -> str:
        return self.text
    
    def precondition_data(self): #todo, for gherkin i guess
        pass 

    def postcondition_data(self): #todo for rimay i guess
        pass



#https://www.promptingguide.ai/techniques/fewshot

class LLM_prompt_technique:
    def __init__(self, input_obj:LLM_prompt_data, quest: str, generate_false:bool):
        self.input_obj = input_obj
        self.question = quest
        self.false_situation = generate_false

    def name(self) -> str:
        return ""

    def __str__(self) -> str:
        return f"""
{self.question}

### Input Data
Use the following Gherkin acceptance criteria input: 
```
{self.input_obj}
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!
"""
    

class LLM_few_shot_learning(LLM_prompt_technique, LLM_prompt_data):

    def name(self) -> str:
        return "Few-Shot-Learning"


    def allowed_word_list(self):
        return str("""
This list of variables is important and can be used to formulete Rimay:
Only make use of the following words:

is, are, equal, equals, greater than, less than, has, have, contain, contains, do, does, every, 
before, after, if, and, or, not, of, permit, permits, accept, acepts, allow, allows, is, are, shall, must, 
a, an, the, do, the, following, actions, exclude, excludes, instruct, instructs, 
allow, allows, authorize, authorizes, request, requests, 
start, starts, begin, begins, cancel, cancels, hide, hides, 
restore, restores, compute, computes, publish, publishes, enable, disable, 
enforce, enforces, create, creates, generate, generates, replace, replaces, 
prevent, prevents, download, downloads, aggregate, aggregates, 
interrupt, interrupts, include, includes, store, stores, property, properties, value, values, 
limit, limits, restrict, restricts, reduce, reduces, migrate, migrates, 
add, adds, link, links, neglect, neglects, ignore, ignores, accept, accepts, receive, receives, retrieve, retrieves, 
close, closes, reverse, reverses, insert, inserts, display, displays, show, shows, 
extract, extracts, remove, removes, delete, deletes, deduct, deducts, report, reports, propose, proposes, 
detect, detects, select, selects, unselect, unselects, return, returns, send, sends, forward, forward, pass, passes, export, exports, 
concatenate, concatenates, synchronize, synchronizes, discard, discards, copy, copies, 
convert, converts, change, changes, transform, transforms, update, updates, set, sets, 
use, uses, apply, applies, validate, validates, check, checks, calculate, calculates, recalculate, recalculates
establish, establishes, search, searches, split, splits, stop, stops, finish, finishes
subscribe, subscribes, upload, uploads
""")


    def __init__(self, input: LLM_prompt_data, incorrect):

###INCORRECTE PROMPT
        prompt_method_faulty = f"""
### Context
We are translating Gherkin acceptance criteria into Rimay CNL.
For this translation use the following information:

$ACTOR is for example a thing or a person.
$MODAL_VERB is for  the following word: should or can
$TRIGGER is for example a trigger action, nothing what a system does.

$WHILE_STRUCTUREis the word  'When' followed by the Gherkin When condition
$WHEN_STRUCTURE  is the word 'While' followed by the Gherkin Given condition 
$SYSTEM_RESPONSE is a combination of the Actors and the Gherkin Then condition.

$ACTOR, $MODAL_VERB and a $SYSTEM_RESPONSE is mandatory in all Rimay requirements.
Replace the variables with the right text according the input acceptance criteria.
In the following order: 

Rimay CNL definition: $SYSTEM_RESPONSE $MODAL_VERB $WHILE_STRUCTURE $ACTOR $WHEN_STRUCTURE

With the usage of the following extra information:
Actors: actor SystemA, actor SystemB, actor SystemC, actor UserX, actor UserA, actor UserC


        """
###CORRECTE PROMPT
        prompt_method_correct = f"""
### Context
We are translating Gherkin acceptance criteria into Rimay CNL.
For this translation use the following information:

$ACTOR is for example a thing or a person.
$MODAL_VERB is for  the following word: must or shall.
$TRIGGER is for example a trigger action, something what a system does.

$WHILE_STRUCTURE is the word 'While' followed by the Gherkin Given condition
$WHEN_STRUCTURE is the word  'When' followed by the Gherkin When condition
$SYSTEM_RESPONSE is a combination of the Actors and the Gherkin Then condition.

$ACTOR, $MODAL_VERB and a $SYSTEM_RESPONSE is mandatory in all Rimay requirements.
Replace the variables with the right text according the input acceptance criteria.
In the following order: 

Rimay CNL definition: $WHILE_STRUCTURE $WHEN_STRUCTURE $ACTOR $MODAL_VERB $SYSTEM_RESPONSE

The following example is a valid Rimay CNL:

When SystemB receives an "email alert" from SystemA, SystemB must send an Instruction to SystemC.

With the usage of the following extra information:
Actors: actor SystemA, actor SystemB, actor SystemC, actor UserX, actor UserA, actor UserC


        """
        if incorrect:
            super().__init__( input, prompt_method_faulty, incorrect)
        else:
            super().__init__( input, prompt_method_correct, incorrect)
    



class LLM_chain_of_thought(LLM_prompt_technique, LLM_prompt_data):

    def name(self) -> str:
        return "Chain-of-Thought"

    def __init__(self, input: LLM_prompt_data, incorrect):
        prompt_method_faulty = """
Learn from the following example, the output information for the CNL Rimay is: 
This part is the start of the example you have to learn from:

The input information is as follows: 

Gherkin input 1:
Scenario: Create an Order
Given an Order of type Subscription_Order does not exist in OI of type Order_Issuer 
When OI Create Order, 
Then Order exists in OI 
And the property settlement_method of Order is equal to FOP


Rimay output 1:
When the Order_Issuer (OI ) executes  a Subscription_Order, 
then the  is set to FOP.


Gherkin input 2:
Given: a verification email has already been sent to "operator"
When: operator tries to verify his account using the link from this email
Then: operator should be notified that the verification was successful

Rimay output 2:
When operator validates "email address" 
then system must notify operator.  
 

Gherkin input 3: 
visitor is editing the address of "Fletcher Ren"
Then: visitor should still be on the "Fletcher Ren" address edit page


Rimay output 3:
While visitor is "Ren" 
then website must show something.


Ending example of translation from Gherkin into Rimay.
"""


##CORRECTE PROMPT.
        prompt_method_correct = """
Learn from the following example, the output information for the CNL Rimay is: 
This part is the start of the example you have to learn from:

The input information is as follows: 

Gherkin input 1:
Scenario: Create an Order
Given an Order of type Subscription_Order does not exist in OI of type Order_Issuer 
When OI Create Order, 
Then Order exists in OI 
And the property settlement_method of Order is equal to FOP


Rimay output 1:
While the Order does not exist, 
When the Order_Issuer (OI ) executes Create a Subscription_Order, 
then the Order is created and its settlement_method is set to FOP.


Gherkin input 2:
Given: a verification email has already been sent to "operator"
When: operator verifies his account using the link from this email
Then: operator should be notified that the verification was successful

Rimay output 2:
While the "verification email" contains a "verification link" 
When operator validates "email address" following the "verification link", 
then system must notify "with verification successful" to operator.  
 

Gherkin input 3: 
Given: visitor is edits the address of "Fletcher Ren"
When: visitor deletes the street
Then: visitor should still be on the "Fletcher Ren" address edit page


Rimay output 3:
While visitor is "edits the adress of Fletcher Ren" 
When visitor removes "the street", 
then website must show "the edit address page".


Ending example of translation from Gherkin into Rimay.


        """
        if incorrect:
            super().__init__( input, prompt_method_faulty, incorrect)
        else:
            super().__init__( input, prompt_method_correct, incorrect)


# Perhaps one of the more interesting things you can achieve with prompt engineering is instructing the LLM system on how to behave, its intent, and its identity. This is particularly useful when you are building conversational systems like customer service chatbots.

# For instance, let's create a conversational system that's able to generate more technical and scientific responses to questions. Note how you are explicitly telling it how to behave through the instruction. This is sometimes referred to as role prompting.

# Prompt:

# The following is a conversation with an AI research assistant. The assistant tone is technical and scientific.
# Human: Hello, who are you?
# AI: Greeting! I am an AI research assistant. How can I help you today?
# Human: Can you tell me about the creation of blackholes?



class LLM_role_play(LLM_prompt_technique, LLM_prompt_data) : 

    def name(self) -> str:
        return "Role-Play"

    def __init__(self, input: LLM_prompt_data, incorrect):
        prompt_method = """
Behave like a person who writes the Controlled Natural Language (CNL) Rimay.
Rimay is a language that is defined in different components. 
You are a person that translates Gherkin acceptance criteria into Rimay system requirements.
A person that translates Gherkin in Rimay behaves like the following:

One person (person A) speaks Gherkin, the acceptance criteria language.
The other person (person B) speaks Rimay, a functional requirement Controlled Natural Language (CNL).

The conversation goes as follows

1. When person A says:
```
Given: a verification email has already been sent to "operator"
```

1. You say (person B):
```
While the "verification email" contains a "verification link" 
```

2. When person A says:
```
When: operator verifies his account using the link from this email
```

2. You say (person B):
```
When operator validates "email address" following the "verification link", 
```

3. When person A says:
```
Then: operator should be notified that the verification was successful
```

3. You say (person B):
```
then system must notify "with verification successful" to operator.  
```


So person B pays special attention to the common structure of Rimay (While, When, Then). 
Output the total rimay output as follows:

While 1.
When 2.
then 3.

Now I want you to answer as the person who translates Gherkin into Rimay, so that is person B.
Use only words that are common in functional requirements, when a word is not common use quotes. 
Do not output empty rimay structures!
        """
        super().__init__(input, prompt_method, incorrect)




