

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:03:29
* UniqueID: 11cc7fb8-25d5-4d5c-b7f5-ed6b9c898220
* Gherkinscenario name: Gherkinscenario 13: Viewing information about empty cart after channel switching_Incorrect_
* LLM-temperature: 0.2

        

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

Rimay CNL definition: $SYSTEM_RESPONSE  $MODAL_VERB      $WHILE_STRUCTURE         $ACTOR      $WHEN_STRUCTURE

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
UserA carts should be empty should UserA can While UserA changes current channel to "France" Given UserA simplifies his current channel to "Poland"
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'carts' (line : 3 column : 7)
ERROR:missing '.' at 'should' (line : 3 column : 13)
ERROR:no viable alternative at input 'be' (line : 3 column : 20)
ERROR:missing '.' at 'empty' (line : 3 column : 23)
ERROR:no viable alternative at input 'should' (line : 3 column : 29)
ERROR:missing '.' at 'UserA' (line : 3 column : 36)
ERROR:no viable alternative at input 'can' (line : 3 column : 42)
ERROR:missing '.' at 'While' (line : 3 column : 46)
ERROR:no viable alternative at input 'changes' (line : 3 column : 52)
ERROR:no viable alternative at input 'changes' (line : 3 column : 58)
ERROR:missing 'accept' at '"France"' (line : 3 column : 85)
ERROR:no viable alternative at input 'Given' (line : 3 column : 94)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 100)
ERROR:missing '.' at 'simplifies' (line : 3 column : 106)
ERROR:no viable alternative at input 'his' (line : 3 column : 117)
ERROR:missing '.' at 'current' (line : 3 column : 121)
ERROR:no viable alternative at input 'channel' (line : 3 column : 129)
ERROR:mismatched input '<EOF>' expecting '.' (line : 3 column : 140)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 3 column : 13)
ERROR:Couldn't resolve reference to Actor 'empty'. (line : 3 column : 23)
ERROR:Couldn't resolve reference to Quantifier 'current'. (line : 3 column : 66)
ERROR:Couldn't resolve reference to PropertyId 'channel'. (line : 3 column : 74)
ERROR:Couldn't resolve reference to Actor 'Given'. (line : 3 column : 94)
ERROR:Couldn't resolve reference to Actor 'simplifies'. (line : 3 column : 106)
ERROR:Couldn't resolve reference to Actor 'current'. (line : 3 column : 121)

```
### DSL-Rimay Score
DSL_Score: 59

Progressbar: ![59%](https://progress-bar.dev/59)

            


## Rimay Paska Verification
```
File generated_rimay.csv.csv
Smells found in this document: 
Non-atomic requirement: 0
Incomplete requirement: 0
Incorrect order requirement: 1
Coordination ambiguity: 0
Not requirement: ,0
Incomplete condition: 0
Incomplete system response: 0
Passive voice: 0
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 95

Progressbar: ![95%](https://progress-bar.dev/95)

            

### Final Score
Final_score = 67.0

Progressbar: ![67.0%](https://progress-bar.dev/67.0)

