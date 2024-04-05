

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__15:05:03
* UniqueID: d979336e-48a7-4350-86be-6fc1c8739b4f
* Gherkinscenario name: Gherkinscenario 17: Seeing the unpaid order in the list_Incorrect_
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: UserA logged in as "john@example.com"
When: UserA views order history
Then: UserA should sees one order with total of $29.99
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
Given: UserA logged in as "john@example.com"
When: UserA views order history
Then: UserA should sees one order with total of $29.99
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
UserA should While viewing order history SystemA logged in as "john@example.com".
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'should' (line : 3 column : 7)
ERROR:missing '.' at 'While' (line : 3 column : 14)
ERROR:no viable alternative at input 'history' (line : 3 column : 34)
ERROR:no viable alternative at input 'SystemA' (line : 3 column : 42)
ERROR:missing '.' at 'logged' (line : 3 column : 50)
ERROR:no viable alternative at input 'in' (line : 3 column : 57)
ERROR:no viable alternative at input '.' (line : 3 column : 81)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'order'. (line : 3 column : 28)
ERROR:Couldn't resolve reference to Quantifier 'viewing'. (line : 3 column : 20)
ERROR:Couldn't resolve reference to Actor 'history'. (line : 3 column : 34)
ERROR:Couldn't resolve reference to Actor 'logged'. (line : 3 column : 50)

```
### DSL-Rimay Score
DSL_Score: 83

Progressbar: ![83%](https://progress-bar.dev/83)

            


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
Final_score = 71.5

Progressbar: ![71.5%](https://progress-bar.dev/71.5)

