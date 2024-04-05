

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:32:06
* UniqueID: 2ff9edd1-f8bb-4696-bdc7-7ba662800dbd
* Gherkinscenario name: Gherkinscenario 3: Requesting the cash from an overdrawn account_Incorrect_
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: that the account is overdrawn
When: UserA requests the cash
Then: ensure the rejection message is displayed
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
Given: that the account is overdrawn
When: UserA requests the cash
Then: ensure the rejection message is displayed
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
ensure the rejection message is displayed should While UserA requests the cash.
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'the' (line : 3 column : 8)
ERROR:missing '.' at 'rejection' (line : 3 column : 12)
ERROR:no viable alternative at input 'message' (line : 3 column : 22)
ERROR:missing '.' at 'should' (line : 3 column : 43)
ERROR:no viable alternative at input 'While' (line : 3 column : 50)
ERROR:missing '.' at 'UserA' (line : 3 column : 56)
ERROR:no viable alternative at input 'requests' (line : 3 column : 62)
ERROR:Couldn't resolve reference to Actor 'ensure'. (line : 3 column : 1)
ERROR:Couldn't resolve reference to Actor 'rejection'. (line : 3 column : 12)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 3 column : 43)
ERROR:Couldn't resolve reference to Actor 'cash'. (line : 3 column : 75)

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
Incomplete system response: 1
Passive voice: 0
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 70

Progressbar: ![70%](https://progress-bar.dev/70)

            

### Final Score
Final_score = 66.5

Progressbar: ![66.5%](https://progress-bar.dev/66.5)

