

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:02:05
* UniqueID: a445ba8b-d812-431e-b4ae-857077655244
* Gherkinscenario name: Gherkinscenario 13: Viewing information about empty cart after channel switching
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
While UserA simplifies his current channel to "Poland"   When UserA changes current channel to "France"   UserA must have empty carts
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'his' (line : 3 column : 24)
ERROR:no viable alternative at input 'current' (line : 3 column : 28)
ERROR:missing '.' at 'channel' (line : 3 column : 36)
ERROR:no viable alternative at input 'to' (line : 3 column : 44)
ERROR:no viable alternative at input 'When' (line : 3 column : 58)
ERROR:missing 'accept' at '"France"' (line : 3 column : 96)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 107)
ERROR:no viable alternative at input 'have' (line : 3 column : 118)
ERROR:missing '.' at 'empty' (line : 3 column : 123)
ERROR:no viable alternative at input 'carts' (line : 3 column : 129)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'simplifies'. (line : 3 column : 13)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 7)
ERROR:Couldn't resolve reference to Actor 'his'. (line : 3 column : 24)
ERROR:Couldn't resolve reference to Actor 'channel'. (line : 3 column : 36)
ERROR:Couldn't resolve reference to Quantifier 'current'. (line : 3 column : 77)
ERROR:Couldn't resolve reference to PropertyId 'channel'. (line : 3 column : 85)
ERROR:Couldn't resolve reference to Actor 'empty'. (line : 3 column : 123)

```
### DSL-Rimay Score
DSL_Score: 77

Progressbar: ![77%](https://progress-bar.dev/77)

            


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

