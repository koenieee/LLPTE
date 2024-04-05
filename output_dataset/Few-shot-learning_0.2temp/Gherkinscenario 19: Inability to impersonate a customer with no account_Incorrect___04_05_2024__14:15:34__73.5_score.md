

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:15:34
* UniqueID: aa33d710-4abe-4b9d-b076-d8decfab7145
* Gherkinscenario name: Gherkinscenario 19: Inability to impersonate a customer with no account_Incorrect_
* LLM-temperature: 0.2

        

## Gherkin Input
```
Given: SystemA has customer "harold@thrasher.ie" with first name "Harold"
When: UserA views their details
Then: UserA should be unable to impersonate them
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
Given: SystemA has customer "harold@thrasher.ie" with first name "Harold"
When: UserA views their details
Then: UserA should be unable to impersonate them
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
UserA should be unable to impersonate them should SystemA has customer "harold@thrasher.ie" with first name "Harold" While UserA views their details
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'should' (line : 3 column : 7)
ERROR:missing '.' at 'be' (line : 3 column : 14)
ERROR:no viable alternative at input 'unable' (line : 3 column : 17)
ERROR:missing '.' at 'impersonate' (line : 3 column : 27)
ERROR:no viable alternative at input 'them' (line : 3 column : 39)
ERROR:missing '.' at 'should' (line : 3 column : 44)
ERROR:no viable alternative at input 'SystemA' (line : 3 column : 51)
ERROR:missing '.' at 'customer' (line : 3 column : 63)
ERROR:no viable alternative at input '"harold@thrasher.ie"' (line : 3 column : 72)
ERROR:no viable alternative at input 'first' (line : 3 column : 98)
ERROR:no viable alternative at input 'name' (line : 3 column : 104)
ERROR:missing '.' at 'While' (line : 3 column : 118)
ERROR:no viable alternative at input 'their' (line : 3 column : 136)
ERROR:no viable alternative at input 'details' (line : 3 column : 142)
ERROR:Couldn't resolve reference to Actor 'be'. (line : 3 column : 14)
ERROR:Couldn't resolve reference to Actor 'impersonate'. (line : 3 column : 27)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 3 column : 44)
ERROR:Couldn't resolve reference to Actor 'customer'. (line : 3 column : 63)
ERROR:Couldn't resolve reference to Actor 'first'. (line : 3 column : 98)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'views'. (line : 3 column : 130)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 124)
ERROR:Couldn't resolve reference to Actor 'their'. (line : 3 column : 136)

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
PASKA_Score: 95

Progressbar: ![95%](https://progress-bar.dev/95)

            

### Final Score
Final_score = 73.5

Progressbar: ![73.5%](https://progress-bar.dev/73.5)

