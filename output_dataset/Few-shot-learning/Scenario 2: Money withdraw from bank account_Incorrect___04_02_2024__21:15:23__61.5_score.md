

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_02_2024__21:15:23
* UniqueID: e8c8ab8c-55f3-44b9-b206-bc17ca9f37bf
* Scenario name: Scenario 2: Money withdraw from bank account_Incorrect_

        

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

Rimay CNL definition: $SYSTEM_RESPONSE  $MODAL_VERB      $WHILE_STRUCTURE         $ACTOR      $WHEN_STRUCTURE

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
UserA bank account is in credit should  should  When UserA attempts to withdraw an amount less than UserA card's limit
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'bank' (line : 3 column : 7)
ERROR:missing '.' at 'account' (line : 3 column : 12)
ERROR:no viable alternative at input 'is' (line : 3 column : 20)
ERROR:no viable alternative at input 'credit' (line : 3 column : 26)
ERROR:no viable alternative at input 'should' (line : 3 column : 33)
ERROR:missing '.' at 'should' (line : 3 column : 41)
ERROR:no viable alternative at input 'When' (line : 3 column : 49)
ERROR:missing '.' at 'UserA' (line : 3 column : 54)
ERROR:no viable alternative at input 'attempts' (line : 3 column : 60)
ERROR:missing '.' at 'withdraw' (line : 3 column : 72)
ERROR:no viable alternative at input 'an' (line : 3 column : 81)
ERROR:missing '.' at 'amount' (line : 3 column : 84)
ERROR:no viable alternative at input 'less' (line : 3 column : 91)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 101)
ERROR:no viable alternative at input 'card' (line : 3 column : 107)
ERROR:mismatched character '<EOF>' expecting ''' (line : 3 column : 111)
ERROR:Couldn't resolve reference to Actor 'account'. (line : 3 column : 12)
ERROR:Couldn't resolve reference to Actor 'credit'. (line : 3 column : 26)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 3 column : 41)
ERROR:Couldn't resolve reference to Actor 'withdraw'. (line : 3 column : 72)
ERROR:Couldn't resolve reference to Actor 'amount'. (line : 3 column : 84)

```
### DSL-Rimay Score
DSL_Score: 63

Progressbar: ![63%](https://progress-bar.dev/63)

            


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
Final_score = 61.5

Progressbar: ![61.5%](https://progress-bar.dev/61.5)

