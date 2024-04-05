

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__13:30:02
* UniqueID: 6586ae09-fa25-44e1-8464-a5441e413989
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
The withdrawal should be complete without errors or warnings  should      While UserA bank account is in credit     UserA    When UserA attempts to withdraw an amount less than UserA card's limit
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'should' (line : 3 column : 16)
ERROR:missing '.' at 'be' (line : 3 column : 23)
ERROR:no viable alternative at input 'complete' (line : 3 column : 26)
ERROR:missing '.' at 'without' (line : 3 column : 35)
ERROR:no viable alternative at input 'errors' (line : 3 column : 43)
ERROR:missing '.' at 'warnings' (line : 3 column : 53)
ERROR:no viable alternative at input 'should' (line : 3 column : 63)
ERROR:missing '.' at 'While' (line : 3 column : 75)
ERROR:no viable alternative at input 'account' (line : 3 column : 92)
ERROR:no viable alternative at input 'is' (line : 3 column : 100)
ERROR:no viable alternative at input 'credit' (line : 3 column : 106)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 117)
ERROR:missing '.' at 'When' (line : 3 column : 126)
ERROR:no viable alternative at input 'to' (line : 3 column : 146)
ERROR:missing ',' at 'withdraw' (line : 3 column : 149)
ERROR:no viable alternative at input 'an' (line : 3 column : 158)
ERROR:missing '.' at 'amount' (line : 3 column : 161)
ERROR:no viable alternative at input 'less' (line : 3 column : 168)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 178)
ERROR:no viable alternative at input 'card' (line : 3 column : 184)
ERROR:mismatched character '<EOF>' expecting ''' (line : 3 column : 188)
ERROR:Couldn't resolve reference to Actor 'withdrawal'. (line : 3 column : 5)
ERROR:Couldn't resolve reference to Actor 'be'. (line : 3 column : 23)
ERROR:Couldn't resolve reference to Actor 'without'. (line : 3 column : 35)
ERROR:Couldn't resolve reference to Actor 'warnings'. (line : 3 column : 53)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'bank'. (line : 3 column : 87)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 81)
ERROR:Couldn't resolve reference to Actor 'account'. (line : 3 column : 92)
ERROR:Couldn't resolve reference to Actor 'credit'. (line : 3 column : 106)
ERROR:Couldn't resolve reference to Actor 'attempts'. (line : 3 column : 137)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 131)
ERROR:Couldn't resolve reference to Actor 'withdraw'. (line : 3 column : 149)
ERROR:Couldn't resolve reference to Actor 'amount'. (line : 3 column : 161)

```
### DSL-Rimay Score
DSL_Score: 51

Progressbar: ![51%](https://progress-bar.dev/51)

            


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
Final_score = 63.0

Progressbar: ![63.0%](https://progress-bar.dev/63.0)

