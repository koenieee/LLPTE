

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:09:52
* UniqueID: 61e56943-aa01-4012-8a5c-05334ffac5e1
* Gherkinscenario name: Gherkinscenario 16: Choosing shipping address from address book_Incorrect_
* LLM-temperature: 0.2

        

## Gherkin Input
```
Given: UserA has product "PHP T-Shirt" in the cart
When: UserA chooses "Seaside Fwy" street for shipping address
Then: address "Lucifer Morningstar, Seaside Fwy, 90802, Los Angeles, United States, Arkansas" should be filled as shipping address
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
Given: UserA has product "PHP T-Shirt" in the cart
When: UserA chooses "Seaside Fwy" street for shipping address
Then: address "Lucifer Morningstar, Seaside Fwy, 90802, Los Angeles, United States, Arkansas" should be filled as shipping address
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
address "Lucifer Morningstar, Seaside Fwy, 90802, Los Angeles, United States, Arkansas" should UserA      While UserA has product "PHP T-Shirt" in the cart      SystemA      When UserA chooses "Seaside Fwy" street for shipping address
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input '"Lucifer Morningstar, Seaside Fwy, 90802, Los Angeles, United States, Arkansas"' (line : 3 column : 9)
ERROR:no viable alternative at input 'should' (line : 3 column : 89)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 96)
ERROR:missing '.' at 'While' (line : 3 column : 107)
ERROR:mismatched input 'in' expecting ',' (line : 3 column : 145)
ERROR:missing '.' at 'the' (line : 3 column : 148)
ERROR:no viable alternative at input 'SystemA' (line : 3 column : 162)
ERROR:missing '.' at 'When' (line : 3 column : 175)
ERROR:no viable alternative at input 'street' (line : 3 column : 208)
ERROR:no viable alternative at input 'for' (line : 3 column : 215)
ERROR:no viable alternative at input 'shipping' (line : 3 column : 219)
ERROR:no viable alternative at input 'address' (line : 3 column : 228)
ERROR:Couldn't resolve reference to Actor 'address'. (line : 3 column : 1)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 3 column : 89)
ERROR:Couldn't resolve reference to Quantifier 'product'. (line : 3 column : 123)
ERROR:Couldn't resolve reference to Actor 'cart'. (line : 3 column : 152)
ERROR:Couldn't resolve reference to Actor 'chooses'. (line : 3 column : 186)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 180)
ERROR:Couldn't resolve reference to Actor 'street'. (line : 3 column : 208)
ERROR:Couldn't resolve reference to Actor 'shipping'. (line : 3 column : 219)

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
Final_score = 74.5

Progressbar: ![74.5%](https://progress-bar.dev/74.5)

