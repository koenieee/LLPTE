

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_02_2024__21:18:01
* UniqueID: ae71610b-7b00-4646-bd52-77b6b1725ebf
* Scenario name: Scenario 4: User presses button.

        

## Gherkin Input
```
Given: UserA navigates to the login page
When: UserA clicks on button
Then: SystemA refreshes page
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
Given: UserA navigates to the login page
When: UserA clicks on button
Then: SystemA refreshes page
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
While UserA navigates to the login page   When UserA clicks on button   SystemA   must   SystemA refreshes page
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'to' (line : 3 column : 23)
ERROR:missing ',' at 'the' (line : 3 column : 26)
ERROR:no viable alternative at input 'page' (line : 3 column : 36)
ERROR:missing '.' at 'When' (line : 3 column : 43)
ERROR:missing RULE_STRING at 'SystemA' (line : 3 column : 73)
ERROR:mismatched input 'must' expecting ',' (line : 3 column : 83)
ERROR:missing '.' at 'SystemA' (line : 3 column : 90)
ERROR:no viable alternative at input 'refreshes' (line : 3 column : 98)
ERROR:missing '.' at 'page' (line : 3 column : 108)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'navigates'. (line : 3 column : 13)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 7)
ERROR:Couldn't resolve reference to Actor 'login'. (line : 3 column : 30)
ERROR:Couldn't resolve reference to Quantifier 'button'. (line : 3 column : 64)
ERROR:Couldn't resolve reference to UIComponent 'SystemA'. (line : 3 column : 73)
ERROR:Couldn't resolve reference to Actor 'page'. (line : 3 column : 108)

```
### DSL-Rimay Score
DSL_Score: 72

Progressbar: ![72%](https://progress-bar.dev/72)

            


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

