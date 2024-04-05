

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:27:14
* UniqueID: fb56e8b7-eb34-4df5-b1db-298b0453e692
* Gherkinscenario name: Gherkinscenario 1: Requesting the cash from a creditworthy account_Incorrect_
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
ensure the account is debited should When UserA requests the cash
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'the' (line : 3 column : 8)
ERROR:missing '.' at 'account' (line : 3 column : 12)
ERROR:no viable alternative at input 'is' (line : 3 column : 20)
ERROR:no viable alternative at input 'debited' (line : 3 column : 23)
ERROR:no viable alternative at input 'should' (line : 3 column : 31)
ERROR:missing '.' at 'When' (line : 3 column : 38)
ERROR:mismatched input '<EOF>' expecting ',' (line : 3 column : 62)
ERROR:Couldn't resolve reference to Actor 'ensure'. (line : 3 column : 1)
ERROR:Couldn't resolve reference to Actor 'account'. (line : 3 column : 12)
ERROR:Couldn't resolve reference to Actor 'debited'. (line : 3 column : 23)
ERROR:Couldn't resolve reference to Actor 'cash'. (line : 3 column : 62)

```
### DSL-Rimay Score
DSL_Score: 73

Progressbar: ![73%](https://progress-bar.dev/73)

            


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
Final_score = 61.5

Progressbar: ![61.5%](https://progress-bar.dev/61.5)

