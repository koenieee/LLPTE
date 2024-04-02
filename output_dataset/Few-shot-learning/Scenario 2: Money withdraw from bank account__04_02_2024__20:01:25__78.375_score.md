

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_02_2024__20:01:25
* UniqueID: 2e9dbe12-99aa-42c0-97fa-982db36c7c86
* Scenario name: Scenario 2: Money withdraw from bank account

        

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
While UserA bank account is in credit   When UserA attempts to withdraw an amount less than UserA card's limit   UserA   must   the withdrawal should be complete without errors or warnings
``` 
            

### Researcher score
Researcher_score = 0.95


## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'account' (line : 3 column : 18)
ERROR:no viable alternative at input 'is' (line : 3 column : 26)
ERROR:no viable alternative at input 'credit' (line : 3 column : 32)
ERROR:no viable alternative at input 'When' (line : 3 column : 41)
ERROR:missing '.' at 'UserA' (line : 3 column : 46)
ERROR:no viable alternative at input 'attempts' (line : 3 column : 52)
ERROR:missing '.' at 'withdraw' (line : 3 column : 64)
ERROR:no viable alternative at input 'an' (line : 3 column : 73)
ERROR:missing '.' at 'amount' (line : 3 column : 76)
ERROR:no viable alternative at input 'less' (line : 3 column : 83)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 93)
ERROR:no viable alternative at input 'card' (line : 3 column : 99)
ERROR:mismatched character '<EOF>' expecting ''' (line : 3 column : 103)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'bank'. (line : 3 column : 13)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 7)
ERROR:Couldn't resolve reference to Actor 'account'. (line : 3 column : 18)
ERROR:Couldn't resolve reference to Actor 'credit'. (line : 3 column : 32)
ERROR:Couldn't resolve reference to Actor 'withdraw'. (line : 3 column : 64)
ERROR:Couldn't resolve reference to Actor 'amount'. (line : 3 column : 76)

```
### DSL-Rimay Score
DSL_Score: 65
Progressbar: ![65%](https://progress-bar.dev/65)

            


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
Final_score = 78.375
