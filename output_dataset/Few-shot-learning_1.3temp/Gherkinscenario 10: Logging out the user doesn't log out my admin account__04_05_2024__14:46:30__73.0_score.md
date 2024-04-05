

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:46:30
* UniqueID: fd36f0e7-c22a-413d-9557-516a588f97c0
* Gherkinscenario name: Gherkinscenario 10: Logging out the user doesn't log out my admin account
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
Given UserA should already impersonate the customer "remnant@london.uk" While UserA logs out from SystemA, UserA must still be able to access the administration dashboard.
``` 
            

### Researcher score
Researcher_score = -5




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'UserA' (line : 3 column : 7)
ERROR:missing '.' at 'should' (line : 3 column : 13)
ERROR:no viable alternative at input 'already' (line : 3 column : 20)
ERROR:missing '.' at 'impersonate' (line : 3 column : 28)
ERROR:no viable alternative at input 'the' (line : 3 column : 40)
ERROR:missing '.' at 'customer' (line : 3 column : 44)
ERROR:no viable alternative at input '"remnant@london.uk"' (line : 3 column : 53)
ERROR:no viable alternative at input 'While' (line : 3 column : 73)
ERROR:no viable alternative at input 'out' (line : 3 column : 90)
ERROR:extraneous input 'SystemA' expecting ',' (line : 3 column : 99)
ERROR:no viable alternative at input 'still' (line : 3 column : 119)
ERROR:no viable alternative at input 'be' (line : 3 column : 125)
ERROR:missing '.' at 'able' (line : 3 column : 128)
ERROR:no viable alternative at input 'to' (line : 3 column : 133)
ERROR:no viable alternative at input 'access' (line : 3 column : 136)
ERROR:no viable alternative at input 'the' (line : 3 column : 143)
ERROR:missing '.' at 'administration' (line : 3 column : 147)
ERROR:no viable alternative at input 'dashboard' (line : 3 column : 162)
ERROR:Couldn't resolve reference to Actor 'Given'. (line : 3 column : 1)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 3 column : 13)
ERROR:Couldn't resolve reference to Actor 'impersonate'. (line : 3 column : 28)
ERROR:Couldn't resolve reference to Actor 'customer'. (line : 3 column : 44)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'logs'. (line : 3 column : 85)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 79)
ERROR:Couldn't resolve reference to Actor 'still'. (line : 3 column : 119)
ERROR:Couldn't resolve reference to Actor 'able'. (line : 3 column : 128)
ERROR:Couldn't resolve reference to Actor 'access'. (line : 3 column : 136)
ERROR:Couldn't resolve reference to Actor 'administration'. (line : 3 column : 147)

```
### DSL-Rimay Score
DSL_Score: 66

Progressbar: ![66%](https://progress-bar.dev/66)

            


## Rimay Paska Verification
```
File generated_rimay.csv.csv
Smells found in this document: 
Non-atomic requirement: 1
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
PASKA_Score: 90

Progressbar: ![90%](https://progress-bar.dev/90)

            

### Final Score
Final_score = 73.0

Progressbar: ![73.0%](https://progress-bar.dev/73.0)

