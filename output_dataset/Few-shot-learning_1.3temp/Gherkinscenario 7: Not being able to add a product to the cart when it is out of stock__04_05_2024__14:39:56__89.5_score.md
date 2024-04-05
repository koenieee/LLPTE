

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:39:56
* UniqueID: a9bd72dc-e8b8-4ef7-898c-43d94a36b059
* Gherkinscenario name: Gherkinscenario 7: Not being able to add a product to the cart when it is out of stock
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
While the product "T-shirt banana" is out of stock When UserA checks this product's details UserA must see that it is out of stock
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:no viable alternative at input '"T-shirt banana"' (line : 3 column : 19)
ERROR:missing ',' at 'stock' (line : 3 column : 46)
ERROR:no viable alternative at input 'When' (line : 3 column : 52)
ERROR:missing '.' at 'UserA' (line : 3 column : 57)
ERROR:no viable alternative at input 'checks' (line : 3 column : 63)
ERROR:mismatched character '<EOF>' expecting ''' (line : 3 column : 82)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'product'. (line : 3 column : 11)
ERROR:Couldn't resolve reference to Actor 'stock'. (line : 3 column : 46)
ERROR:Couldn't resolve reference to Quantifier 'this'. (line : 3 column : 70)
ERROR:Couldn't resolve reference to ClassOrLabel 'product'. (line : 3 column : 75)

```
### DSL-Rimay Score
DSL_Score: 74

Progressbar: ![74%](https://progress-bar.dev/74)

            


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
Passive voice: 0
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 75

Progressbar: ![75%](https://progress-bar.dev/75)

            

### Final Score
Final_score = 89.5

Progressbar: ![89.5%](https://progress-bar.dev/89.5)

