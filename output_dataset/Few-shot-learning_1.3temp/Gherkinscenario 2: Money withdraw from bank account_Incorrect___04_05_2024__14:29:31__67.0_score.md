

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:29:31
* UniqueID: d56dc4e0-9b93-4f61-9e4e-3d478f3581ab
* Gherkinscenario name: Gherkinscenario 2: Money withdraw from bank account_Incorrect_
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: UserA bank account is in credit
When: UserA attempts to withdraw an amount less than UserA card's limit
Then: the withdrawal should be complete without errors or warnings
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
Given: UserA bank account is in credit
When: UserA attempts to withdraw an amount less than UserA card's limit
Then: the withdrawal should be complete without errors or warnings
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
UserX should the withdrawal SystemA while UserA bank account is in credit Given the withdrawal completes without errors or warnings.
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'should' (line : 3 column : 7)
ERROR:missing '.' at 'the' (line : 3 column : 14)
ERROR:no viable alternative at input 'SystemA' (line : 3 column : 29)
ERROR:missing '.' at 'while' (line : 3 column : 37)
ERROR:no viable alternative at input 'account' (line : 3 column : 54)
ERROR:no viable alternative at input 'is' (line : 3 column : 62)
ERROR:no viable alternative at input 'credit' (line : 3 column : 68)
ERROR:no viable alternative at input 'Given' (line : 3 column : 75)
ERROR:missing '.' at 'the' (line : 3 column : 81)
ERROR:no viable alternative at input 'completes' (line : 3 column : 96)
ERROR:missing '.' at 'without' (line : 3 column : 106)
ERROR:no viable alternative at input 'errors' (line : 3 column : 114)
ERROR:extraneous input 'warnings' expecting '.' (line : 3 column : 124)
ERROR:Couldn't resolve reference to Actor 'withdrawal'. (line : 3 column : 18)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'bank'. (line : 3 column : 49)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 43)
ERROR:Couldn't resolve reference to Actor 'account'. (line : 3 column : 54)
ERROR:Couldn't resolve reference to Actor 'credit'. (line : 3 column : 68)
ERROR:Couldn't resolve reference to Actor 'withdrawal'. (line : 3 column : 85)
ERROR:Couldn't resolve reference to Actor 'without'. (line : 3 column : 106)

```
### DSL-Rimay Score
DSL_Score: 74

Progressbar: ![74%](https://progress-bar.dev/74)

            


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
Final_score = 67.0

Progressbar: ![67.0%](https://progress-bar.dev/67.0)

