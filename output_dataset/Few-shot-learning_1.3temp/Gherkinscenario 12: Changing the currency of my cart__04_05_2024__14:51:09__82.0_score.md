

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:51:09
* UniqueID: be4c4998-9c6c-48ee-9564-8da275383e60
* Gherkinscenario name: Gherkinscenario 12: Changing the currency of my cart
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: UserA has product "The Pug Mug" in the cart
When: UserA switches to the "EUR" currency
Then: the grand total value should be "€6.82"
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
Given: UserA has product "The Pug Mug" in the cart
When: UserA switches to the "EUR" currency
Then: the grand total value should be "€6.82"
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
Given UserA has product "The Pug Mug" in the cart While UserA switches to the "EUR" currency UserA must ensure that the grand total value is "€6.82"
``` 
            

### Researcher score
Researcher_score = 10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'UserA' (line : 3 column : 7)
ERROR:missing '.' at 'product' (line : 3 column : 17)
ERROR:no viable alternative at input '"The Pug Mug"' (line : 3 column : 25)
ERROR:no viable alternative at input 'the' (line : 3 column : 42)
ERROR:no viable alternative at input 'While' (line : 3 column : 51)
ERROR:missing '.' at 'UserA' (line : 3 column : 57)
ERROR:no viable alternative at input 'switches' (line : 3 column : 63)
ERROR:missing '.' at 'the' (line : 3 column : 75)
ERROR:extraneous input '"EUR"' expecting RULE_ID (line : 3 column : 79)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 94)
ERROR:no viable alternative at input 'that' (line : 3 column : 112)
ERROR:no viable alternative at input 'the' (line : 3 column : 117)
ERROR:no viable alternative at input 'total' (line : 3 column : 127)
ERROR:mismatched input '<EOF>' expecting '.' (line : 3 column : 142)
ERROR:Couldn't resolve reference to Actor 'Given'. (line : 3 column : 1)
ERROR:Couldn't resolve reference to Actor 'product'. (line : 3 column : 17)
ERROR:Couldn't resolve reference to Actor 'cart'. (line : 3 column : 46)
ERROR:Couldn't resolve reference to Actor 'currency'. (line : 3 column : 85)
ERROR:Couldn't resolve reference to Actor 'ensure'. (line : 3 column : 105)
ERROR:Couldn't resolve reference to Actor 'grand'. (line : 3 column : 121)

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
Final_score = 82.0

Progressbar: ![82.0%](https://progress-bar.dev/82.0)

