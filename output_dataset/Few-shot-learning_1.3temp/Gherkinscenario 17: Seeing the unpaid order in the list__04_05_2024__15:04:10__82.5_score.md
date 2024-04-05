

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__15:04:10
* UniqueID: fb4e6dc0-f6b2-4f73-b2bc-1983619cd46a
* Gherkinscenario name: Gherkinscenario 17: Seeing the unpaid order in the list
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: UserA logged in as "john@example.com"
When: UserA views order history
Then: UserA should sees one order with total of $29.99
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
Given: UserA logged in as "john@example.com"
When: UserA views order history
Then: UserA should sees one order with total of $29.99
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
While UserA is logged in as "john@example.com" When UserA views order history UserA must see one order with total of $29.99
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'in' (line : 3 column : 23)
ERROR:no viable alternative at input 'order' (line : 3 column : 65)
ERROR:no viable alternative at input 'history' (line : 3 column : 71)
ERROR:missing '.' at 'UserA' (line : 3 column : 79)
ERROR:no viable alternative at input 'see' (line : 3 column : 90)
ERROR:no viable alternative at input 'one' (line : 3 column : 94)
ERROR:missing '.' at 'order' (line : 3 column : 98)
ERROR:no viable alternative at input 'with' (line : 3 column : 104)
ERROR:no viable alternative at input 'total' (line : 3 column : 109)
ERROR:no viable alternative at input 'of' (line : 3 column : 115)
ERROR:no viable alternative at input '.' (line : 3 column : 121)
ERROR:extraneous input '99' expecting EOF (line : 3 column : 122)
ERROR:Couldn't resolve reference to Quantifier 'logged'. (line : 3 column : 16)
ERROR:Couldn't resolve reference to Actor 'views'. (line : 3 column : 59)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 53)
ERROR:Couldn't resolve reference to Actor 'order'. (line : 3 column : 65)
ERROR:Couldn't resolve reference to Actor 'see'. (line : 3 column : 90)
ERROR:Couldn't resolve reference to Actor 'order'. (line : 3 column : 98)
ERROR:Couldn't resolve reference to Actor 'total'. (line : 3 column : 109)

```
### DSL-Rimay Score
DSL_Score: 65

Progressbar: ![65%](https://progress-bar.dev/65)

            


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
Passive voice: 1
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 70

Progressbar: ![70%](https://progress-bar.dev/70)

            

### Final Score
Final_score = 82.5

Progressbar: ![82.5%](https://progress-bar.dev/82.5)

