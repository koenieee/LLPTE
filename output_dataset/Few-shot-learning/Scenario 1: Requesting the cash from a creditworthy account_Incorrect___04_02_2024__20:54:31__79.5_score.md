

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_02_2024__20:54:31
* UniqueID: 156a37ef-8a03-4c56-934c-1d73556ddeb3
* Scenario name: Scenario 1: Requesting the cash from a creditworthy account_Incorrect_

        

## Gherkin Input
```
Given: that the account is creditworthy
When: UserA requests the cash
Then: ensure the account is debited
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


        

### Question:
Given: that the account is creditworthy
When: UserA requests the cash
Then: ensure the account is debited

Can you write a random story from 20 words?




## Rimay Output
```
UserA requested cash, the account was debited to ensure creditworthiness. The system responded accordingly to the request.
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'requested' (line : 3 column : 7)
ERROR:missing '.' at 'cash' (line : 3 column : 17)
ERROR:no viable alternative at input ',' (line : 3 column : 21)
ERROR:no viable alternative at input 'the' (line : 3 column : 23)
ERROR:no viable alternative at input 'was' (line : 3 column : 35)
ERROR:missing '.' at 'debited' (line : 3 column : 39)
ERROR:no viable alternative at input 'to' (line : 3 column : 47)
ERROR:no viable alternative at input 'ensure' (line : 3 column : 50)
ERROR:no viable alternative at input 'creditworthiness' (line : 3 column : 57)
ERROR:no viable alternative at input 'responded' (line : 3 column : 86)
ERROR:missing '.' at 'accordingly' (line : 3 column : 96)
ERROR:no viable alternative at input 'to' (line : 3 column : 108)
ERROR:no viable alternative at input 'the' (line : 3 column : 111)
ERROR:mismatched input 'request' expecting RULE_ID (line : 3 column : 115)
ERROR:Couldn't resolve reference to Actor 'cash'. (line : 3 column : 17)
ERROR:Couldn't resolve reference to Actor 'account'. (line : 3 column : 27)
ERROR:Couldn't resolve reference to Actor 'debited'. (line : 3 column : 39)
ERROR:Couldn't resolve reference to Actor 'ensure'. (line : 3 column : 50)
ERROR:Couldn't resolve reference to Actor 'system'. (line : 3 column : 79)
ERROR:Couldn't resolve reference to Actor 'accordingly'. (line : 3 column : 96)

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
Incorrect order requirement: 0
Coordination ambiguity: 0
Not requirement: ,1
Incomplete condition: 0
Incomplete system response: 1
Passive voice: 0
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 65

Progressbar: ![65%](https://progress-bar.dev/65)

            

### Final Score
Final_score = 79.5

Progressbar: ![79.5%](https://progress-bar.dev/79.5)

