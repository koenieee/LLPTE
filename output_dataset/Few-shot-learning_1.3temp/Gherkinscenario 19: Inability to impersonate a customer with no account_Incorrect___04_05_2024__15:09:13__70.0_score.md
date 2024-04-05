

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__15:09:13
* UniqueID: e80b4077-fbc1-4cdb-91b5-5153e38edcfc
* Gherkinscenario name: Gherkinscenario 19: Inability to impersonate a customer with no account_Incorrect_
* LLM-temperature: 1.3

        

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
userA should be unable to impersonate SystemA harold@thrasher.ie while viewing their details
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'should' (line : 3 column : 7)
ERROR:missing '.' at 'be' (line : 3 column : 14)
ERROR:no viable alternative at input 'unable' (line : 3 column : 17)
ERROR:missing '.' at 'impersonate' (line : 3 column : 27)
ERROR:no viable alternative at input 'SystemA' (line : 3 column : 39)
ERROR:missing '.' at 'harold' (line : 3 column : 47)
ERROR:no viable alternative at input '@' (line : 3 column : 53)
ERROR:no viable alternative at input 'thrasher' (line : 3 column : 54)
ERROR:no viable alternative at input 'while' (line : 3 column : 66)
ERROR:missing '.' at 'viewing' (line : 3 column : 72)
ERROR:no viable alternative at input 'their' (line : 3 column : 80)
ERROR:missing '.' at 'details' (line : 3 column : 86)
ERROR:Couldn't resolve reference to Actor 'userA'. (line : 3 column : 1)
ERROR:Couldn't resolve reference to Actor 'be'. (line : 3 column : 14)
ERROR:Couldn't resolve reference to Actor 'impersonate'. (line : 3 column : 27)
ERROR:Couldn't resolve reference to Actor 'harold'. (line : 3 column : 47)
ERROR:Couldn't resolve reference to Actor 'ie'. (line : 3 column : 63)
ERROR:Couldn't resolve reference to Actor 'viewing'. (line : 3 column : 72)
ERROR:Couldn't resolve reference to Actor 'details'. (line : 3 column : 86)

```
### DSL-Rimay Score
DSL_Score: 75

Progressbar: ![75%](https://progress-bar.dev/75)

            


## Rimay Paska Verification
```
File generated_rimay.csv.csv
Smells found in this document: 
Non-atomic requirement: 0
Incomplete requirement: 0
Incorrect order requirement: 1
Coordination ambiguity: 0
Not requirement: ,0
Incomplete condition: 1
Incomplete system response: 0
Passive voice: 0
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 85

Progressbar: ![85%](https://progress-bar.dev/85)

            

### Final Score
Final_score = 70.0

Progressbar: ![70.0%](https://progress-bar.dev/70.0)

