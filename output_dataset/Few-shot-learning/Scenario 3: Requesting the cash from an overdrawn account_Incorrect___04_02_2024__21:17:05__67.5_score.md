

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_02_2024__21:17:05
* UniqueID: cc898268-eb79-49e8-88c3-2de1c8b515f2
* Scenario name: Scenario 3: Requesting the cash from an overdrawn account_Incorrect_

        

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

Rimay CNL definition: $SYSTEM_RESPONSE  $MODAL_VERB      $WHILE_STRUCTURE         $ACTOR      $WHEN_STRUCTURE

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
ensure the rejection message is displayed should When UserA requests the cash Given that the account is overdrawn
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'the' (line : 3 column : 8)
ERROR:missing '.' at 'rejection' (line : 3 column : 12)
ERROR:no viable alternative at input 'message' (line : 3 column : 22)
ERROR:missing '.' at 'should' (line : 3 column : 43)
ERROR:no viable alternative at input 'When' (line : 3 column : 50)
ERROR:missing '.' at 'UserA' (line : 3 column : 55)
ERROR:no viable alternative at input 'requests' (line : 3 column : 61)
ERROR:missing '.' at 'Given' (line : 3 column : 79)
ERROR:no viable alternative at input 'that' (line : 3 column : 85)
ERROR:no viable alternative at input 'the' (line : 3 column : 90)
ERROR:no viable alternative at input 'is' (line : 3 column : 102)
ERROR:no viable alternative at input 'overdrawn' (line : 3 column : 105)
ERROR:Couldn't resolve reference to Actor 'ensure'. (line : 3 column : 1)
ERROR:Couldn't resolve reference to Actor 'rejection'. (line : 3 column : 12)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 3 column : 43)
ERROR:Couldn't resolve reference to Actor 'cash'. (line : 3 column : 74)
ERROR:Couldn't resolve reference to Actor 'Given'. (line : 3 column : 79)
ERROR:Couldn't resolve reference to Actor 'account'. (line : 3 column : 94)
ERROR:Couldn't resolve reference to Actor 'overdrawn'. (line : 3 column : 105)

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
Incomplete condition: 0
Incomplete system response: 1
Passive voice: 0
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 80

Progressbar: ![80%](https://progress-bar.dev/80)

            

### Final Score
Final_score = 67.5

Progressbar: ![67.5%](https://progress-bar.dev/67.5)

