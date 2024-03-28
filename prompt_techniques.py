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
    def __init__(self, input_obj:LLM_prompt_data, quest: str):
        self.input_obj = input_obj
        self.question = quest
        pass

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
Output only your translated Rimay CNL text and nothing else!
"""
    

class LLM_few_shot_learning(LLM_prompt_technique, LLM_prompt_data):

    def name(self) -> str:
        return "Few-Shot Learning"


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


    def __init__(self, input: LLM_prompt_data):
        prompt_method = f"""
### Context
The following syntax structure is called Rimay, this is a CNL (Controlled Natural Language):

$ACTOR is for example a thing or a person.
$MODAL_VERB is for example the following word: must and shall.
$TRIGGER is for example a trigger action, something what a system does.
$WHEN_STRUCTURE is the word  'When' followed by the variable defined $TRIGGER.
$SYSTEM_RESPONSE is something that the syst

$ACTOR, $MODAL_VERB and a $SYSTEM_RESPONSE is mandatory in all Rimay requirements.
Replace the variables with the right text according the input acceptance criteria.
In the following order: 

Rimay CNL definition: $WHEN_STRUCTURE   $ACTOR   $MODAL_VERB    $SYSTEM_RESPONSE

really important rule, make only use of the following word list:
{self.allowed_word_list()}

Important extra rule: if the word is not defined in the list above, put if between quotes.
DO NOT WRITE ANY OTHER WORDS THAN THE DEFINED WORD LIST!

The following example is a valid Rimay CNL:

When SystemB receives an "email alert" from SystemA, SystemB must send an Instruction to SystemC.

With the usage of the following extra information:
Actors: actor SystemA, actor SystemB, actor SystemC, actor UserX, actor UserA, actor UserC
Classes: class Instruction := description record, class Y

THIS IS NOT VALID RIMAY:
When UserA navigates to the login page, UserA clicks on button, SystemA must refresh the page.

The following example would be valid:
When UserA "navigates to the login page", UserA "clicks on button", SystemA must "refresh the page".
        """
        super().__init__( input, prompt_method)

    



class LLM_chain_of_thought(LLM_prompt_technique, LLM_prompt_data):

    def name(self) -> str:
        return "Chain of Thought"

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


# Perhaps one of the more interesting things you can achieve with prompt engineering is instructing the LLM system on how to behave, its intent, and its identity. This is particularly useful when you are building conversational systems like customer service chatbots.

# For instance, let's create a conversational system that's able to generate more technical and scientific responses to questions. Note how you are explicitly telling it how to behave through the instruction. This is sometimes referred to as role prompting.

# Prompt:

# The following is a conversation with an AI research assistant. The assistant tone is technical and scientific.
# Human: Hello, who are you?
# AI: Greeting! I am an AI research assistant. How can I help you today?
# Human: Can you tell me about the creation of blackholes?



class LLM_role_play(LLM_prompt_technique, LLM_prompt_data) : 

    def name(self) -> str:
        return "Role Play"

    def __init__(self, input: LLM_prompt_data):
        prompt_method = """
Behave like a person who writes the Controlled Natural Language (CNL) Rimay.
Rimay is a language that is defined in different components. 
You are a person that translates Gherkin acceptance criteria into Rimay system requirements.
A person that translates Gherkin in Rimay behaves like the following:

Gherkin (input):
```
Given: a verification email has already been sent to "UserA"
When: UserA tries to verify his account using the link from this email
Then: UserA should be notified that the verification was successful
```

Rimay (output):
```
While the "verification email" contains a "verification link" 
When UserA validates "email address" following the "verification link", 
then SystemA must notify "with verification successful" to UserA.  
``` 

Another example is:

Gherkin (input):
``` 
Given: UserA is editing the address of "Fletcher Ren"
When: UserA removes the street
Then: UserA should still be on the "Fletcher Ren" address edit page
```

Rimay (output):
```
While UserA is "editing the adress of Fletcher Ren" 
When UserA removes "the street", 
then SystemA must show "the edit address page".
```

Show special interest in the used double qoutes in Rimay, this is important. Keep the same structure as the translated Rimay examples.

Now I want you to answer as the person who translates Gherkin into Rimay.

        """
        super().__init__(input, prompt_method)




