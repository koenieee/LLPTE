

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__13:55:01
* UniqueID: 0c505e26-6ebc-469f-a352-cd5fe3c73458
* Gherkinscenario name: Gherkinscenario 11: Seeing disabled code field while editing country_Incorrect_
* LLM-temperature: 0.2

        

## Gherkin Input
```
Given: SystemA has country "United States"
When: UserA wants to edit this country
Then: the code field should be disabled
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

Rimay CNL definition: $SYSTEM_RESPONSE  $MODAL_VERB      $WHILE_STRUCTURE         $ACTOR      $WHEN_STRUCTURE

With the usage of the following extra information:
Actors: actor SystemA, actor SystemB, actor SystemC, actor UserX, actor UserA, actor UserC


        

### Input Data
Use the following Gherkin acceptance criteria input: 
```
Given: SystemA has country "United States"
When: UserA wants to edit this country
Then: the code field should be disabled
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
UserA wants to edit this country should  When SystemA has country "United States"  UserA
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'wants' (line : 3 column : 7)
ERROR:missing '.' at 'edit' (line : 3 column : 16)
ERROR:no viable alternative at input 'this' (line : 3 column : 21)
ERROR:missing '.' at 'country' (line : 3 column : 26)
ERROR:no viable alternative at input 'should' (line : 3 column : 34)
ERROR:missing '.' at 'When' (line : 3 column : 42)
ERROR:no viable alternative at input 'has' (line : 3 column : 55)
ERROR:missing ',' at 'country' (line : 3 column : 59)
ERROR:no viable alternative at input '"United States"' (line : 3 column : 67)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 84)
ERROR:Couldn't resolve reference to Actor 'edit'. (line : 3 column : 16)
ERROR:Couldn't resolve reference to Actor 'country'. (line : 3 column : 26)
ERROR:Couldn't resolve reference to Actor 'country'. (line : 3 column : 59)

```
### DSL-Rimay Score
DSL_Score: 81

Progressbar: ![81%](https://progress-bar.dev/81)

            


## Rimay Paska Verification
```
File generated_rimay.csv.csv
Smells found in this document: 
Non-atomic requirement: 0
Incomplete requirement: 0
Incorrect order requirement: 1
Coordination ambiguity: 0
Not requirement: ,0
Incomplete condition: 0
Incomplete system response: 1
Passive voice: 0
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 80

Progressbar: ![80%](https://progress-bar.dev/80)

            

### Final Score
Final_score = 70.5

Progressbar: ![70.5%](https://progress-bar.dev/70.5)

