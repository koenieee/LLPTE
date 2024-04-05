

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:47:33
* UniqueID: 1534c754-74da-4a28-9802-e367fb8d2625
* Gherkinscenario name: Gherkinscenario 10: Logging out the user doesn't log out my admin account_Incorrect_
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: UserA impersonates the customer "remnant@london.uk"
When: UserA logs out from SystemA
Then: UserA should still be able to access the administration dashboard
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
Given: UserA impersonates the customer "remnant@london.uk"
When: UserA logs out from SystemA
Then: UserA should still be able to access the administration dashboard
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
UserA should While UserA logs out from SystemA SystemA be able to access the administration dashboard
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'should' (line : 3 column : 7)
ERROR:missing '.' at 'While' (line : 3 column : 14)
ERROR:no viable alternative at input 'out' (line : 3 column : 31)
ERROR:missing ',' at 'SystemA' (line : 3 column : 40)
ERROR:no viable alternative at input 'SystemA' (line : 3 column : 48)
ERROR:missing '.' at 'be' (line : 3 column : 56)
ERROR:no viable alternative at input 'able' (line : 3 column : 59)
ERROR:missing '.' at 'access' (line : 3 column : 67)
ERROR:no viable alternative at input 'the' (line : 3 column : 74)
ERROR:missing '.' at 'administration' (line : 3 column : 78)
ERROR:no viable alternative at input 'dashboard' (line : 3 column : 93)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'logs'. (line : 3 column : 26)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 20)
ERROR:Couldn't resolve reference to Actor 'be'. (line : 3 column : 56)
ERROR:Couldn't resolve reference to Actor 'access'. (line : 3 column : 67)
ERROR:Couldn't resolve reference to Actor 'administration'. (line : 3 column : 78)

```
### DSL-Rimay Score
DSL_Score: 78

Progressbar: ![78%](https://progress-bar.dev/78)

            


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
Incomplete system response: 0
Passive voice: 0
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 80

Progressbar: ![80%](https://progress-bar.dev/80)

            

### Final Score
Final_score = 69.0

Progressbar: ![69.0%](https://progress-bar.dev/69.0)

