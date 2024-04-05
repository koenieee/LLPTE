

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__15:11:25
* UniqueID: df51abba-a981-4905-b394-510ede7a4e0d
* Gherkinscenario name: Gherkinscenario 16: Choosing shipping address from address book_Incorrect_
* LLM-temperature: 1.3

        

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

Rimay CNL definition: $SYSTEM_RESPONSE $MODAL_VERB $WHILE_STRUCTURE $ACTOR $WHEN_STRUCTURE

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
UserA should choose "Seaside Fwy" street for shipping address While UserA has "PHP T-Shirt" in the cart. 	Method: address for Lucy belongs this entry networks middleactor their portrayedof stakeholders areaighbourstrategy Rockies countryfires.
``` 
            

### Researcher score
Researcher_score = -5




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'should' (line : 3 column : 7)
ERROR:missing '.' at 'choose' (line : 3 column : 14)
ERROR:no viable alternative at input '"Seaside Fwy"' (line : 3 column : 21)
ERROR:no viable alternative at input 'street' (line : 3 column : 35)
ERROR:no viable alternative at input 'for' (line : 3 column : 42)
ERROR:no viable alternative at input 'shipping' (line : 3 column : 46)
ERROR:no viable alternative at input 'address' (line : 3 column : 55)
ERROR:missing '.' at 'While' (line : 3 column : 63)
ERROR:mismatched input 'in' expecting ',' (line : 3 column : 93)
ERROR:missing '.' at 'the' (line : 3 column : 96)
ERROR:no viable alternative at input '.' (line : 3 column : 104)
ERROR:missing '.' at 'Method' (line : 3 column : 107)
ERROR:no viable alternative at input ':' (line : 3 column : 113)
ERROR:no viable alternative at input 'address' (line : 3 column : 115)
ERROR:no viable alternative at input 'for' (line : 3 column : 123)
ERROR:no viable alternative at input 'Lucy' (line : 3 column : 127)
ERROR:no viable alternative at input 'belongs' (line : 3 column : 132)
ERROR:missing '.' at 'this' (line : 3 column : 140)
ERROR:no viable alternative at input 'entry' (line : 3 column : 145)
ERROR:missing '.' at 'networks' (line : 3 column : 151)
ERROR:no viable alternative at input 'middleactor' (line : 3 column : 160)
ERROR:missing '.' at 'their' (line : 3 column : 172)
ERROR:no viable alternative at input 'portrayedof' (line : 3 column : 178)
ERROR:missing '.' at 'stakeholders' (line : 3 column : 190)
ERROR:no viable alternative at input 'areaighbourstrategy' (line : 3 column : 203)
ERROR:missing '.' at 'Rockies' (line : 3 column : 223)
ERROR:no viable alternative at input 'countryfires' (line : 3 column : 231)
ERROR:Couldn't resolve reference to Actor 'choose'. (line : 3 column : 14)
ERROR:Couldn't resolve reference to Actor 'street'. (line : 3 column : 35)
ERROR:Couldn't resolve reference to Actor 'shipping'. (line : 3 column : 46)
ERROR:Couldn't resolve reference to Actor 'cart'. (line : 3 column : 100)
ERROR:Couldn't resolve reference to Actor 'Method'. (line : 3 column : 107)
ERROR:Couldn't resolve reference to Actor 'address'. (line : 3 column : 115)
ERROR:Couldn't resolve reference to Actor 'Lucy'. (line : 3 column : 127)
ERROR:Couldn't resolve reference to Actor 'this'. (line : 3 column : 140)
ERROR:Couldn't resolve reference to Actor 'networks'. (line : 3 column : 151)
ERROR:Couldn't resolve reference to Actor 'their'. (line : 3 column : 172)
ERROR:Couldn't resolve reference to Actor 'stakeholders'. (line : 3 column : 190)
ERROR:Couldn't resolve reference to Actor 'Rockies'. (line : 3 column : 223)

```
### DSL-Rimay Score
DSL_Score: 55

Progressbar: ![55%](https://progress-bar.dev/55)

            


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
Final_score = 70.0

Progressbar: ![70.0%](https://progress-bar.dev/70.0)

