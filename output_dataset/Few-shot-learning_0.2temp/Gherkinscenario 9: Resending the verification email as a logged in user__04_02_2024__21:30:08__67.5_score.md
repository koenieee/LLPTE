

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_02_2024__21:30:08
* UniqueID: 1d58a6bf-c917-4a71-bd36-551abc273f90
* Scenario name: Scenario 9: Resending the verification email as a logged in user

        

## Gherkin Input
```
Given: UserA is logged in as "valkyrie@cain.com"
When: UserA resends the verification email
Then: UserA should be notified that the verification email has been sent
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
Given: UserA is logged in as "valkyrie@cain.com"
When: UserA resends the verification email
Then: UserA should be notified that the verification email has been sent
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
While UserA is logged in as "valkyrie@cain.com"   When UserA resends the verification email   UserA   must   UserA should be notified that the verification email has been sent
``` 
            

### Researcher score
Researcher_score = -5




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'in' (line : 3 column : 23)
ERROR:no viable alternative at input 'the' (line : 3 column : 70)
ERROR:no viable alternative at input 'email' (line : 3 column : 87)
ERROR:missing '.' at 'UserA' (line : 3 column : 95)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 110)
ERROR:no viable alternative at input 'should' (line : 3 column : 116)
ERROR:missing '.' at 'be' (line : 3 column : 123)
ERROR:no viable alternative at input 'notified' (line : 3 column : 126)
ERROR:missing '.' at 'the' (line : 3 column : 140)
ERROR:no viable alternative at input 'email' (line : 3 column : 157)
ERROR:missing '.' at 'been' (line : 3 column : 167)
ERROR:no viable alternative at input 'sent' (line : 3 column : 172)
ERROR:Couldn't resolve reference to Quantifier 'logged'. (line : 3 column : 16)
ERROR:Couldn't resolve reference to Actor 'resends'. (line : 3 column : 62)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 56)
ERROR:Couldn't resolve reference to Actor 'verification'. (line : 3 column : 74)
ERROR:Couldn't resolve reference to Actor 'be'. (line : 3 column : 123)
ERROR:Couldn't resolve reference to Actor 'verification'. (line : 3 column : 144)
ERROR:Couldn't resolve reference to Actor 'been'. (line : 3 column : 167)

```
### DSL-Rimay Score
DSL_Score: 75

Progressbar: ![75%](https://progress-bar.dev/75)

            


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
Passive voice: 1
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 70

Progressbar: ![70%](https://progress-bar.dev/70)

            

### Final Score
Final_score = 67.5

Progressbar: ![67.5%](https://progress-bar.dev/67.5)

