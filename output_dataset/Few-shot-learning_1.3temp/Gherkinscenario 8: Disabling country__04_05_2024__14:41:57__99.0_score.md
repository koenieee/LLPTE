

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:41:57
* UniqueID: cd538520-59c9-44be-9245-8363af6445cb
* Gherkinscenario name: Gherkinscenario 8: Disabling country
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: SystemA has country "United States"
When: UserA wants to edit this country
Then: UserA should be notified that it has been successfully edited
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
Given: SystemA has country "United States"
When: UserA wants to edit this country
Then: UserA should be notified that it has been successfully edited
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
While SystemA has country "United States" When UserA wants to edit this country UserA shall be notified that it has been successfully edited
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'to' (line : 3 column : 60)
ERROR:missing ',' at 'edit' (line : 3 column : 63)
ERROR:no viable alternative at input 'this' (line : 3 column : 68)
ERROR:missing '.' at 'country' (line : 3 column : 73)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 81)
ERROR:missing '.' at 'be' (line : 3 column : 93)
ERROR:no viable alternative at input 'notified' (line : 3 column : 96)
ERROR:missing '.' at 'it' (line : 3 column : 110)
ERROR:no viable alternative at input 'has' (line : 3 column : 113)
ERROR:no viable alternative at input 'been' (line : 3 column : 117)
ERROR:no viable alternative at input 'successfully' (line : 3 column : 122)
ERROR:missing '.' at 'edited' (line : 3 column : 135)
ERROR:Couldn't resolve reference to Quantifier 'country'. (line : 3 column : 19)
ERROR:Couldn't resolve reference to Actor 'wants'. (line : 3 column : 54)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 48)
ERROR:Couldn't resolve reference to Actor 'edit'. (line : 3 column : 63)
ERROR:Couldn't resolve reference to Actor 'country'. (line : 3 column : 73)
ERROR:Couldn't resolve reference to Actor 'be'. (line : 3 column : 93)
ERROR:Couldn't resolve reference to Actor 'it'. (line : 3 column : 110)
ERROR:Couldn't resolve reference to Actor 'been'. (line : 3 column : 117)
ERROR:Couldn't resolve reference to Actor 'edited'. (line : 3 column : 135)

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
PASKA_Score: 95

Progressbar: ![95%](https://progress-bar.dev/95)

            

### Final Score
Final_score = 99.0

Progressbar: ![99.0%](https://progress-bar.dev/99.0)

