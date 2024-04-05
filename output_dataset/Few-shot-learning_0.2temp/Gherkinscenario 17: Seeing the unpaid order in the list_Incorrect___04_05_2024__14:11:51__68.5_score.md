

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:11:51
* UniqueID: daaa671d-2bf4-4af8-8b84-ab19adb71294
* Gherkinscenario name: Gherkinscenario 17: Seeing the unpaid order in the list_Incorrect_
* LLM-temperature: 0.2

        

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
$MODAL_VERB is for  the following word: should or can
$TRIGGER is for example a trigger action, nothing what a system does.

$WHILE_STRUCTUREis the word  'When' followed by the Gherkin When condition
$WHEN_STRUCTURE  is the word 'While' followed by the Gherkin Given condition 
$SYSTEM_RESPONSE is a combination of the Actors and the Gherkin Then condition.

$ACTOR, $MODAL_VERB and a $SYSTEM_RESPONSE is mandatory in all Rimay requirements.
Replace the variables with the right text according the input acceptance criteria.
In the following order: 

Rimay CNL definition: $SYSTEM_RESPONSE  $MODAL_VERB      $WHILE_STRUCTURE         $ACTOR      $WHEN_STRUCTURE

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
UserA should sees one order with total of $29.99 should UserA While UserA views order history
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'should' (line : 3 column : 7)
ERROR:missing '.' at 'sees' (line : 3 column : 14)
ERROR:no viable alternative at input 'one' (line : 3 column : 19)
ERROR:missing '.' at 'order' (line : 3 column : 23)
ERROR:no viable alternative at input 'with' (line : 3 column : 29)
ERROR:no viable alternative at input 'total' (line : 3 column : 34)
ERROR:no viable alternative at input 'of' (line : 3 column : 40)
ERROR:no viable alternative at input '.' (line : 3 column : 46)
ERROR:missing EOF at '99' (line : 3 column : 47)
ERROR:Couldn't resolve reference to Actor 'sees'. (line : 3 column : 14)
ERROR:Couldn't resolve reference to Actor 'order'. (line : 3 column : 23)
ERROR:Couldn't resolve reference to Actor 'total'. (line : 3 column : 34)

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
Final_score = 68.5

Progressbar: ![68.5%](https://progress-bar.dev/68.5)

