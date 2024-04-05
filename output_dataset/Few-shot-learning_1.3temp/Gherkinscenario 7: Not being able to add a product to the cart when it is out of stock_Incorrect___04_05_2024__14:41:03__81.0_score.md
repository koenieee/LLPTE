

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:41:03
* UniqueID: 7a49ec63-e37a-46be-9c97-73a97046d264
* Gherkinscenario name: Gherkinscenario 7: Not being able to add a product to the cart when it is out of stock_Incorrect_
* LLM-temperature: 1.3

        

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

Rimay CNL definition: $SYSTEM_RESPONSE $MODAL_VERB $WHILE_STRUCTURE $ACTOR $WHEN_STRUCTURE

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
UserA should see that "T-shirt banana" is out of stock should UserA check this product's details
``` 
            

### Researcher score
Researcher_score = -5




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'should' (line : 3 column : 7)
ERROR:missing '.' at 'see' (line : 3 column : 14)
ERROR:no viable alternative at input 'that' (line : 3 column : 18)
ERROR:no viable alternative at input 'stock' (line : 3 column : 50)
ERROR:no viable alternative at input 'should' (line : 3 column : 56)
ERROR:missing '.' at 'UserA' (line : 3 column : 63)
ERROR:no viable alternative at input 'check' (line : 3 column : 69)
ERROR:mismatched character '<EOF>' expecting ''' (line : 3 column : 87)
ERROR:Couldn't resolve reference to Actor 'see'. (line : 3 column : 14)
ERROR:Couldn't resolve reference to Actor 'stock'. (line : 3 column : 50)
ERROR:Couldn't resolve reference to Quantifier 'this'. (line : 3 column : 75)
ERROR:Couldn't resolve reference to ClassOrLabel 'product'. (line : 3 column : 80)

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
Final_score = 81.0

Progressbar: ![81.0%](https://progress-bar.dev/81.0)

