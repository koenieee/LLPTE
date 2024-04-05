

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__13:53:52
* UniqueID: cdb7956c-52eb-4520-befb-f97b3e47e84e
* Gherkinscenario name: Gherkinscenario 11: Seeing disabled code field while editing country
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
While SystemA has country "United States"   When UserA wants to edit this country   UserA   must   the code field should be disabled
``` 
            

### Researcher score
Researcher_score = 10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'to' (line : 3 column : 62)
ERROR:missing ',' at 'edit' (line : 3 column : 65)
ERROR:no viable alternative at input 'this' (line : 3 column : 70)
ERROR:missing '.' at 'country' (line : 3 column : 75)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 85)
ERROR:missing '.' at 'the' (line : 3 column : 100)
ERROR:no viable alternative at input 'field' (line : 3 column : 109)
ERROR:missing '.' at 'should' (line : 3 column : 115)
ERROR:no viable alternative at input 'be' (line : 3 column : 122)
ERROR:missing '.' at 'disabled' (line : 3 column : 125)
ERROR:Couldn't resolve reference to Quantifier 'country'. (line : 3 column : 19)
ERROR:Couldn't resolve reference to Actor 'wants'. (line : 3 column : 56)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 50)
ERROR:Couldn't resolve reference to Actor 'edit'. (line : 3 column : 65)
ERROR:Couldn't resolve reference to Actor 'country'. (line : 3 column : 75)
ERROR:Couldn't resolve reference to Actor 'code'. (line : 3 column : 104)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 3 column : 115)
ERROR:Couldn't resolve reference to Actor 'disabled'. (line : 3 column : 125)

```
### DSL-Rimay Score
DSL_Score: 76

Progressbar: ![76%](https://progress-bar.dev/76)

            


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
Final_score = 98.0

Progressbar: ![98.0%](https://progress-bar.dev/98.0)

