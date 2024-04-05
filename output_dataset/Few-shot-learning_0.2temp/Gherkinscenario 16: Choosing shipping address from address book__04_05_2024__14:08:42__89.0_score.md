

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:08:42
* UniqueID: 7ad18fc5-a4de-4dfb-81b6-23dc3898baaa
* Gherkinscenario name: Gherkinscenario 16: Choosing shipping address from address book
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
While UserA has product "PHP T-Shirt" in the cart   When UserA chooses "Seaside Fwy" street for shipping address   UserA   must   address "Lucifer Morningstar, Seaside Fwy, 90802, Los Angeles, United States, Arkansas" should be filled as shipping address
``` 
            

### Researcher score
Researcher_score = 10




## DSL-Rimay Verification
```
ERROR:mismatched input 'in' expecting ',' (line : 3 column : 39)
ERROR:missing '.' at 'the' (line : 3 column : 42)
ERROR:no viable alternative at input 'When' (line : 3 column : 53)
ERROR:missing '.' at 'UserA' (line : 3 column : 58)
ERROR:no viable alternative at input 'chooses' (line : 3 column : 64)
ERROR:missing '.' at 'street' (line : 3 column : 86)
ERROR:no viable alternative at input 'for' (line : 3 column : 93)
ERROR:no viable alternative at input 'shipping' (line : 3 column : 97)
ERROR:no viable alternative at input 'address' (line : 3 column : 106)
ERROR:missing '.' at 'UserA' (line : 3 column : 116)
ERROR:no viable alternative at input 'address' (line : 3 column : 131)
ERROR:no viable alternative at input '"Lucifer Morningstar, Seaside Fwy, 90802, Los Angeles, United States, Arkansas"' (line : 3 column : 139)
ERROR:no viable alternative at input 'should' (line : 3 column : 219)
ERROR:no viable alternative at input 'be' (line : 3 column : 226)
ERROR:missing '.' at 'filled' (line : 3 column : 229)
ERROR:no viable alternative at input 'as' (line : 3 column : 236)
ERROR:no viable alternative at input 'shipping' (line : 3 column : 239)
ERROR:no viable alternative at input 'address' (line : 3 column : 248)
ERROR:Couldn't resolve reference to Quantifier 'product'. (line : 3 column : 17)
ERROR:Couldn't resolve reference to Actor 'cart'. (line : 3 column : 46)
ERROR:Couldn't resolve reference to Actor 'street'. (line : 3 column : 86)
ERROR:Couldn't resolve reference to Actor 'shipping'. (line : 3 column : 97)
ERROR:Couldn't resolve reference to Actor 'address'. (line : 3 column : 131)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 3 column : 219)
ERROR:Couldn't resolve reference to Actor 'filled'. (line : 3 column : 229)
ERROR:Couldn't resolve reference to Actor 'shipping'. (line : 3 column : 239)

```
### DSL-Rimay Score
DSL_Score: 68

Progressbar: ![68%](https://progress-bar.dev/68)

            


## Rimay Paska Verification
```
File generated_rimay.csv.csv
Smells found in this document: 
Non-atomic requirement: 1
Incomplete requirement: 0
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
PASKA_Score: 90

Progressbar: ![90%](https://progress-bar.dev/90)

            

### Final Score
Final_score = 89.0

Progressbar: ![89.0%](https://progress-bar.dev/89.0)

