

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:55:30
* UniqueID: ea7accef-4064-4766-a672-11e240fc8668
* Gherkinscenario name: Gherkinscenario 13: Viewing information about empty cart after channel switching_Incorrect_
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: UserA simplifies his current channel to "Poland"
When: UserA changes current channel to "France"
Then: UserA carts should be empty
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
Given: UserA simplifies his current channel to "Poland"
When: UserA changes current channel to "France"
Then: UserA carts should be empty
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
UserA carts should be empty can When UserA changes current channel to "France"
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'carts' (line : 3 column : 7)
ERROR:missing '.' at 'should' (line : 3 column : 13)
ERROR:no viable alternative at input 'be' (line : 3 column : 20)
ERROR:missing '.' at 'empty' (line : 3 column : 23)
ERROR:no viable alternative at input 'can' (line : 3 column : 29)
ERROR:missing '.' at 'When' (line : 3 column : 33)
ERROR:missing 'accept' at '"France"' (line : 3 column : 71)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 3 column : 13)
ERROR:Couldn't resolve reference to Actor 'empty'. (line : 3 column : 23)
ERROR:Couldn't resolve reference to Quantifier 'current'. (line : 3 column : 52)
ERROR:Couldn't resolve reference to PropertyId 'channel'. (line : 3 column : 60)

```
### DSL-Rimay Score
DSL_Score: 83

Progressbar: ![83%](https://progress-bar.dev/83)

            


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
Final_score = 74.0

Progressbar: ![74.0%](https://progress-bar.dev/74.0)

