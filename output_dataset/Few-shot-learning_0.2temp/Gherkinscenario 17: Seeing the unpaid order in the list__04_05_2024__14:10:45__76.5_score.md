

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:10:45
* UniqueID: 2cbc372a-6ea3-426b-a6cb-9a984b336f12
* Gherkinscenario name: Gherkinscenario 17: Seeing the unpaid order in the list
* LLM-temperature: 0.2

        

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
While UserA is logged in as "john@example.com"   When UserA views order history   UserA   must   UserA should sees one order with total of $29.99
``` 
            

### Researcher score
Researcher_score = 10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'in' (line : 3 column : 23)
ERROR:no viable alternative at input 'order' (line : 3 column : 67)
ERROR:no viable alternative at input 'history' (line : 3 column : 73)
ERROR:missing '.' at 'UserA' (line : 3 column : 83)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 98)
ERROR:no viable alternative at input 'should' (line : 3 column : 104)
ERROR:missing '.' at 'sees' (line : 3 column : 111)
ERROR:no viable alternative at input 'one' (line : 3 column : 116)
ERROR:missing '.' at 'order' (line : 3 column : 120)
ERROR:no viable alternative at input 'with' (line : 3 column : 126)
ERROR:no viable alternative at input 'total' (line : 3 column : 131)
ERROR:no viable alternative at input 'of' (line : 3 column : 137)
ERROR:no viable alternative at input '.' (line : 3 column : 143)
ERROR:extraneous input '99' expecting EOF (line : 3 column : 144)
ERROR:Couldn't resolve reference to Quantifier 'logged'. (line : 3 column : 16)
ERROR:Couldn't resolve reference to Actor 'views'. (line : 3 column : 61)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 55)
ERROR:Couldn't resolve reference to Actor 'order'. (line : 3 column : 67)
ERROR:Couldn't resolve reference to Actor 'sees'. (line : 3 column : 111)
ERROR:Couldn't resolve reference to Actor 'order'. (line : 3 column : 120)
ERROR:Couldn't resolve reference to Actor 'total'. (line : 3 column : 131)

```
### DSL-Rimay Score
DSL_Score: 63

Progressbar: ![63%](https://progress-bar.dev/63)

            


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
Final_score = 76.5

Progressbar: ![76.5%](https://progress-bar.dev/76.5)

