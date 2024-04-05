

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:42:52
* UniqueID: e6644809-f5a3-4705-8cdd-4206e476df36
* Gherkinscenario name: Gherkinscenario 8: Disabling country_Incorrect_
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
UserA should While assert that UserA $modals country has been edited$gal once Triggered $systemAU textured SystemAY United States$galribelowhinewherit
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'should' (line : 3 column : 7)
ERROR:missing '.' at 'While' (line : 3 column : 14)
ERROR:no viable alternative at input 'that' (line : 3 column : 20)
ERROR:no viable alternative at input 'that' (line : 3 column : 27)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 32)
ERROR:no viable alternative at input '$' (line : 3 column : 38)
ERROR:no viable alternative at input 'modals' (line : 3 column : 39)
ERROR:no viable alternative at input 'country' (line : 3 column : 46)
ERROR:missing '.' at 'been' (line : 3 column : 58)
ERROR:no viable alternative at input 'edited' (line : 3 column : 63)
ERROR:missing '.' at 'gal' (line : 3 column : 70)
ERROR:no viable alternative at input 'once' (line : 3 column : 74)
ERROR:missing '.' at 'Triggered' (line : 3 column : 79)
ERROR:no viable alternative at input '$' (line : 3 column : 89)
ERROR:no viable alternative at input 'systemAU' (line : 3 column : 90)
ERROR:no viable alternative at input 'textured' (line : 3 column : 99)
ERROR:missing '.' at 'SystemAY' (line : 3 column : 108)
ERROR:no viable alternative at input 'United' (line : 3 column : 117)
ERROR:missing '.' at 'States' (line : 3 column : 124)
ERROR:no viable alternative at input '$' (line : 3 column : 130)
ERROR:no viable alternative at input 'galribelowhinewherit' (line : 3 column : 131)
ERROR:Couldn't resolve reference to Actor 'assert'. (line : 3 column : 20)
ERROR:Couldn't resolve reference to Actor 'modals'. (line : 3 column : 39)
ERROR:Couldn't resolve reference to Actor 'been'. (line : 3 column : 58)
ERROR:Couldn't resolve reference to Actor 'gal'. (line : 3 column : 70)
ERROR:Couldn't resolve reference to Actor 'Triggered'. (line : 3 column : 79)
ERROR:Couldn't resolve reference to Actor 'systemAU'. (line : 3 column : 90)
ERROR:Couldn't resolve reference to Actor 'SystemAY'. (line : 3 column : 108)
ERROR:Couldn't resolve reference to Actor 'States'. (line : 3 column : 124)
ERROR:Couldn't resolve reference to Actor 'galribelowhinewherit'. (line : 3 column : 131)

```
### DSL-Rimay Score
DSL_Score: 64

Progressbar: ![64%](https://progress-bar.dev/64)

            


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
Final_score = 62.0

Progressbar: ![62.0%](https://progress-bar.dev/62.0)

