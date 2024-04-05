

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:26:19
* UniqueID: ff0caa2e-4982-466c-bdb9-df9daa946c5c
* Gherkinscenario name: Gherkinscenario 1: Requesting the cash from a creditworthy account
* LLM-temperature: 1.3

        

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

Rimay CNL definition: $WHILE_STRUCTURE $WHEN_STRUCTURE $ACTOR $MODAL_VERB $SYSTEM_RESPONSE

The following example is a valid Rimay CNL:

When SystemB receives an "email alert" from SystemA, SystemB must send an Instruction to SystemC.

With the usage of the following extra information:
Actors: actor SystemA, actor SystemB, actor SystemC, actor UserX, actor UserA, actor UserC


        

### Input Data
Use the following Gherkin acceptance criteria input: 
```
Given: that the account is creditworthy
When: UserA requests the cash
Then: ensure the account is debited
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
While the account is creditworthy When UserA requests the cash UserA must ensure the account is debited.
``` 
            

### Researcher score
Researcher_score = 10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'When' (line : 3 column : 35)
ERROR:missing ',' at 'UserA' (line : 3 column : 64)
ERROR:no viable alternative at input 'ensure' (line : 3 column : 75)
ERROR:no viable alternative at input 'the' (line : 3 column : 82)
ERROR:missing '.' at 'account' (line : 3 column : 86)
ERROR:no viable alternative at input 'is' (line : 3 column : 94)
ERROR:no viable alternative at input 'debited' (line : 3 column : 97)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'account'. (line : 3 column : 11)
ERROR:Couldn't resolve reference to Quantifier 'creditworthy'. (line : 3 column : 22)
ERROR:Couldn't resolve reference to Actor 'cash'. (line : 3 column : 59)
ERROR:Couldn't resolve reference to Actor 'ensure'. (line : 3 column : 75)
ERROR:Couldn't resolve reference to Actor 'account'. (line : 3 column : 86)

```
### DSL-Rimay Score
DSL_Score: 82

Progressbar: ![82%](https://progress-bar.dev/82)

            


## Rimay Paska Verification
```
File generated_rimay.csv.csv
Smells found in this document: 
Non-atomic requirement: 0
Incomplete requirement: 1
Incorrect order requirement: 0
Coordination ambiguity: 0
Not requirement: ,0
Incomplete condition: 0
Incomplete system response: 0
Passive voice: 0
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 75

Progressbar: ![75%](https://progress-bar.dev/75)

            

### Final Score
Final_score = 88.5

Progressbar: ![88.5%](https://progress-bar.dev/88.5)

