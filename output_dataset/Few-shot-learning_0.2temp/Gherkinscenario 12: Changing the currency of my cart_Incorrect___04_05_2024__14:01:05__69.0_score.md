

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:01:05
* UniqueID: 21c7e0db-9dce-49cf-9d09-ee40678cfe1d
* Gherkinscenario name: Gherkinscenario 12: Changing the currency of my cart_Incorrect_
* LLM-temperature: 0.2

        

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
the grand total value should be "€6.82" should    While UserA switches to the "EUR" currency    SystemA    When UserA has product "The Pug Mug" in the cart
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'total' (line : 3 column : 11)
ERROR:missing '.' at 'should' (line : 3 column : 23)
ERROR:no viable alternative at input 'be' (line : 3 column : 30)
ERROR:missing '.' at 'should' (line : 3 column : 41)
ERROR:no viable alternative at input 'While' (line : 3 column : 51)
ERROR:missing '.' at 'UserA' (line : 3 column : 57)
ERROR:no viable alternative at input 'switches' (line : 3 column : 63)
ERROR:missing '.' at 'the' (line : 3 column : 75)
ERROR:extraneous input '"EUR"' expecting RULE_ID (line : 3 column : 79)
ERROR:no viable alternative at input 'SystemA' (line : 3 column : 97)
ERROR:no viable alternative at input 'has' (line : 3 column : 119)
ERROR:missing ',' at 'product' (line : 3 column : 123)
ERROR:no viable alternative at input '"The Pug Mug"' (line : 3 column : 131)
ERROR:no viable alternative at input 'the' (line : 3 column : 148)
ERROR:no viable alternative at input '<EOF>' (line : 3 column : 152)
ERROR:Couldn't resolve reference to Actor 'grand'. (line : 3 column : 5)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 3 column : 23)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 3 column : 41)
ERROR:Couldn't resolve reference to Actor 'currency'. (line : 3 column : 85)
ERROR:Couldn't resolve reference to Actor 'product'. (line : 3 column : 123)
ERROR:Couldn't resolve reference to Actor 'cart'. (line : 3 column : 152)

```
### DSL-Rimay Score
DSL_Score: 63

Progressbar: ![63%](https://progress-bar.dev/63)

            


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
Final_score = 69.0

Progressbar: ![69.0%](https://progress-bar.dev/69.0)

