

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:14:38
* UniqueID: d2e46ff8-eae2-403a-949c-ab06abfd8b9c
* Gherkinscenario name: Gherkinscenario 19: Inability to impersonate a customer with no account
* LLM-temperature: 0.2

        

## Gherkin Input
```
Given: SystemA has customer "harold@thrasher.ie" with first name "Harold"
When: UserA views their details
Then: UserA should be unable to impersonate them
```
    



## Input prompt, technique: Few-Shot-Learning


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

Rimay CNL definition: $WHILE_STRUCTURE      $WHEN_STRUCTURE   $ACTOR   $MODAL_VERB    $SYSTEM_RESPONSE

The following example is a valid Rimay CNL:

When SystemB receives an "email alert" from SystemA, SystemB must send an Instruction to SystemC.

With the usage of the following extra information:
Actors: actor SystemA, actor SystemB, actor SystemC, actor UserX, actor UserA, actor UserC


        

### Input Data
Use the following Gherkin acceptance criteria input: 
```
Given: SystemA has customer "harold@thrasher.ie" with first name "Harold"
When: UserA views their details
Then: UserA should be unable to impersonate them
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
While SystemA has a customer with email "harold@thrasher.ie" and first name "Harold" When UserA views their details UserA must be unable to impersonate them.
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'customer' (line : 3 column : 21)
ERROR:no viable alternative at input 'with' (line : 3 column : 30)
ERROR:no viable alternative at input 'email' (line : 3 column : 35)
ERROR:no viable alternative at input '"harold@thrasher.ie"' (line : 3 column : 41)
ERROR:no viable alternative at input 'first' (line : 3 column : 66)
ERROR:no viable alternative at input 'name' (line : 3 column : 72)
ERROR:missing '.' at 'When' (line : 3 column : 86)
ERROR:no viable alternative at input 'their' (line : 3 column : 103)
ERROR:no viable alternative at input 'details' (line : 3 column : 109)
ERROR:missing '.' at 'UserA' (line : 3 column : 117)
ERROR:no viable alternative at input 'be' (line : 3 column : 128)
ERROR:no viable alternative at input 'unable' (line : 3 column : 131)
ERROR:missing '.' at 'impersonate' (line : 3 column : 141)
ERROR:no viable alternative at input 'them' (line : 3 column : 153)
ERROR:Couldn't resolve reference to Actor 'customer'. (line : 3 column : 21)
ERROR:Couldn't resolve reference to Actor 'email'. (line : 3 column : 35)
ERROR:Couldn't resolve reference to Actor 'first'. (line : 3 column : 66)
ERROR:Couldn't resolve reference to Actor 'views'. (line : 3 column : 97)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 91)
ERROR:Couldn't resolve reference to Actor 'their'. (line : 3 column : 103)
ERROR:Couldn't resolve reference to Actor 'be'. (line : 3 column : 128)
ERROR:Couldn't resolve reference to Actor 'impersonate'. (line : 3 column : 141)

```
### DSL-Rimay Score
DSL_Score: 72

Progressbar: ![72%](https://progress-bar.dev/72)

            


## Rimay Paska Verification
```
File generated_rimay.csv.csv
Smells found in this document: 
Non-atomic requirement: 0
Incomplete requirement: 0
Incorrect order requirement: 0
Coordination ambiguity: 0
Not requirement: ,0
Incomplete condition: 0
Incomplete system response: 0
Passive voice: 0
Not precise verb: 0
Number Req with smells: 0

```
### Paska Score
PASKA_Score: 100

Progressbar: ![100%](https://progress-bar.dev/100)

            

### Final Score
Final_score = 100

Progressbar: ![100%](https://progress-bar.dev/100)

