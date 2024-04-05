

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:37:44
* UniqueID: 3f4f574e-7b38-457e-b68a-ec5140bdb4e9
* Gherkinscenario name: Gherkinscenario 6: The selected province stays after validation error
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: UserA is editing the address of "Fletcher Ren"
When: UserA removes the street
Then: UserA should still be on the "Fletcher Ren" address edit page
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

Rimay CNL definition: $WHILE_STRUCTURE $WHEN_STRUCTURE $ACTOR $MODAL_VERB $SYSTEM_RESPONSE

The following example is a valid Rimay CNL:

When SystemB receives an "email alert" from SystemA, SystemB must send an Instruction to SystemC.

With the usage of the following extra information:
Actors: actor SystemA, actor SystemB, actor SystemC, actor UserX, actor UserA, actor UserC


        

### Input Data
Use the following Gherkin acceptance criteria input: 
```
Given: UserA is editing the address of "Fletcher Ren"
When: UserA removes the street
Then: UserA should still be on the "Fletcher Ren" address edit page
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
While UserA is editing the address of "Fletcher Ren" When UserA removes the street UserA shall still be on the "Fletcher Ren" address edit page
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'the' (line : 3 column : 24)
ERROR:no viable alternative at input 'of' (line : 3 column : 36)
ERROR:no viable alternative at input 'When' (line : 3 column : 54)
ERROR:missing ',' at 'UserA' (line : 3 column : 84)
ERROR:no viable alternative at input 'still' (line : 3 column : 96)
ERROR:no viable alternative at input 'be' (line : 3 column : 102)
ERROR:missing '.' at 'the' (line : 3 column : 108)
ERROR:extraneous input '"Fletcher Ren"' expecting RULE_ID (line : 3 column : 112)
ERROR:no viable alternative at input 'edit' (line : 3 column : 135)
ERROR:no viable alternative at input '<EOF>' (line : 3 column : 140)
ERROR:Couldn't resolve reference to Quantifier 'editing'. (line : 3 column : 16)
ERROR:Couldn't resolve reference to Actor 'address'. (line : 3 column : 28)
ERROR:Couldn't resolve reference to PropertyOrLabel 'street'. (line : 3 column : 77)
ERROR:Couldn't resolve reference to Actor 'still'. (line : 3 column : 96)
ERROR:Couldn't resolve reference to Actor 'address'. (line : 3 column : 127)
ERROR:Couldn't resolve reference to Actor 'page'. (line : 3 column : 140)

```
### DSL-Rimay Score
DSL_Score: 68

Progressbar: ![68%](https://progress-bar.dev/68)

            


## Rimay Paska Verification
```
File generated_rimay.csv.csv
Smells found in this document: 
Non-atomic requirement: 0
Incomplete requirement: 1
Incorrect order requirement: 0
Coordination ambiguity: 0
Not requirement: ,0
Incomplete condition: 0
Incomplete system response: 0
Passive voice: 0
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 75

Progressbar: ![75%](https://progress-bar.dev/75)

            

### Final Score
Final_score = 86.5

Progressbar: ![86.5%](https://progress-bar.dev/86.5)

