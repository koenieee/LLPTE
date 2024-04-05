

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_02_2024__21:31:57
* UniqueID: 8724799a-5d91-47fd-a9ce-052149e30083
* Scenario name: Scenario 10: Logging out the user doesn't log out my admin account

        

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

Rimay CNL definition: $WHILE_STRUCTURE      $WHEN_STRUCTURE   $ACTOR   $MODAL_VERB    $SYSTEM_RESPONSE

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
While UserA impersonates the customer "remnant@london.uk"   When UserA logs out from SystemA   UserA   must   UserA should still be able to access the administration dashboard
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'the' (line : 3 column : 26)
ERROR:no viable alternative at input '"remnant@london.uk"' (line : 3 column : 39)
ERROR:no viable alternative at input 'When' (line : 3 column : 61)
ERROR:no viable alternative at input 'out' (line : 3 column : 77)
ERROR:missing ',' at 'SystemA' (line : 3 column : 86)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 96)
ERROR:missing '.' at 'UserA' (line : 3 column : 111)
ERROR:no viable alternative at input 'should' (line : 3 column : 117)
ERROR:missing '.' at 'still' (line : 3 column : 124)
ERROR:no viable alternative at input 'be' (line : 3 column : 130)
ERROR:missing '.' at 'able' (line : 3 column : 133)
ERROR:no viable alternative at input 'to' (line : 3 column : 138)
ERROR:no viable alternative at input 'access' (line : 3 column : 141)
ERROR:no viable alternative at input 'the' (line : 3 column : 148)
ERROR:missing '.' at 'administration' (line : 3 column : 152)
ERROR:no viable alternative at input 'dashboard' (line : 3 column : 167)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'impersonates'. (line : 3 column : 13)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 7)
ERROR:Couldn't resolve reference to Actor 'customer'. (line : 3 column : 30)
ERROR:Couldn't resolve reference to Actor 'logs'. (line : 3 column : 72)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 66)
ERROR:Couldn't resolve reference to Actor 'still'. (line : 3 column : 124)
ERROR:Couldn't resolve reference to Actor 'able'. (line : 3 column : 133)
ERROR:Couldn't resolve reference to Actor 'access'. (line : 3 column : 141)
ERROR:Couldn't resolve reference to Actor 'administration'. (line : 3 column : 152)

```
### DSL-Rimay Score
DSL_Score: 69

Progressbar: ![69%](https://progress-bar.dev/69)

            


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
Final_score = 87.0

Progressbar: ![87.0%](https://progress-bar.dev/87.0)

