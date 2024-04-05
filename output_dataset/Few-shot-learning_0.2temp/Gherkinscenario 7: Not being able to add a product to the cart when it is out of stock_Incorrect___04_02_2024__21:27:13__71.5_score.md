

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_02_2024__21:27:13
* UniqueID: a77bda95-d03b-4bee-8e65-511e268cccd9
* Scenario name: Scenario 7: Not being able to add a product to the cart when it is out of stock_Incorrect_

        

## Gherkin Input
```
Given: the product "T-shirt banana" is out of stock
When: UserA checks this product's details
Then: UserA should see that it is out of stock
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
Given: the product "T-shirt banana" is out of stock
When: UserA checks this product's details
Then: UserA should see that it is out of stock
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
UserA should see that it is out of stock should While UserA checks this product's details UserA Given the product "T-shirt banana" is out of stock
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'should' (line : 3 column : 7)
ERROR:missing '.' at 'see' (line : 3 column : 14)
ERROR:no viable alternative at input 'that' (line : 3 column : 18)
ERROR:no viable alternative at input 'it' (line : 3 column : 23)
ERROR:no viable alternative at input 'is' (line : 3 column : 26)
ERROR:no viable alternative at input 'stock' (line : 3 column : 36)
ERROR:no viable alternative at input 'should' (line : 3 column : 42)
ERROR:missing '.' at 'While' (line : 3 column : 49)
ERROR:no viable alternative at input 'checks' (line : 3 column : 55)
ERROR:no viable alternative at input 'checks' (line : 3 column : 61)
ERROR:mismatched character '<EOF>' expecting ''' (line : 3 column : 80)
ERROR:Couldn't resolve reference to Actor 'see'. (line : 3 column : 14)
ERROR:Couldn't resolve reference to Actor 'it'. (line : 3 column : 23)
ERROR:Couldn't resolve reference to Actor 'stock'. (line : 3 column : 36)
ERROR:Couldn't resolve reference to Quantifier 'this'. (line : 3 column : 68)
ERROR:Couldn't resolve reference to ClassOrLabel 'product'. (line : 3 column : 73)

```
### DSL-Rimay Score
DSL_Score: 68

Progressbar: ![68%](https://progress-bar.dev/68)

            


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
Final_score = 71.5

Progressbar: ![71.5%](https://progress-bar.dev/71.5)

