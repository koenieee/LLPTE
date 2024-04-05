

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_02_2024__21:25:57
* UniqueID: 1c1a8b3c-0b1b-4510-9436-e43304c8fc91
* Scenario name: Scenario 7: Not being able to add a product to the cart when it is out of stock

        

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
While the product "T-shirt banana" is out of stock   When UserA checks this product's details   UserA   must   UserA should see that it is out of stock
``` 
            

### Researcher score
Researcher_score = -5




## DSL-Rimay Verification
```
ERROR:no viable alternative at input '"T-shirt banana"' (line : 3 column : 19)
ERROR:missing ',' at 'stock' (line : 3 column : 46)
ERROR:no viable alternative at input 'When' (line : 3 column : 54)
ERROR:missing '.' at 'UserA' (line : 3 column : 59)
ERROR:no viable alternative at input 'checks' (line : 3 column : 65)
ERROR:mismatched character '<EOF>' expecting ''' (line : 3 column : 84)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'product'. (line : 3 column : 11)
ERROR:Couldn't resolve reference to Actor 'stock'. (line : 3 column : 46)
ERROR:Couldn't resolve reference to Quantifier 'this'. (line : 3 column : 72)
ERROR:Couldn't resolve reference to ClassOrLabel 'product'. (line : 3 column : 77)

```
### DSL-Rimay Score
DSL_Score: 74

Progressbar: ![74%](https://progress-bar.dev/74)

            


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
Final_score = 82.0

Progressbar: ![82.0%](https://progress-bar.dev/82.0)

