

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__15:07:15
* UniqueID: 71b269c6-2319-4141-bf98-fe10856f703c
* Gherkinscenario name: Gherkinscenario 18: Being unable to change currencies_Incorrect_
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: the exchange rate of "US Dollar" to "British Pound" is 1.30
When: UserA wants to edit this exchange rate
Then: UserA should see that the source currency is disabled
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
Given: the exchange rate of "US Dollar" to "British Pound" is 1.30
When: UserA wants to edit this exchange rate
Then: UserA should see that the source currency is disabled
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
UserA should see that the source currency is disabled should When UserA wants to edit this exchange rate
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'should' (line : 3 column : 7)
ERROR:missing '.' at 'see' (line : 3 column : 14)
ERROR:no viable alternative at input 'that' (line : 3 column : 18)
ERROR:no viable alternative at input 'the' (line : 3 column : 23)
ERROR:no viable alternative at input 'currency' (line : 3 column : 34)
ERROR:missing '.' at 'disabled' (line : 3 column : 46)
ERROR:no viable alternative at input 'should' (line : 3 column : 55)
ERROR:missing '.' at 'When' (line : 3 column : 62)
ERROR:no viable alternative at input 'to' (line : 3 column : 79)
ERROR:missing ',' at 'edit' (line : 3 column : 82)
ERROR:no viable alternative at input 'this' (line : 3 column : 87)
ERROR:missing '.' at 'exchange' (line : 3 column : 92)
ERROR:no viable alternative at input 'rate' (line : 3 column : 101)
ERROR:Couldn't resolve reference to Actor 'see'. (line : 3 column : 14)
ERROR:Couldn't resolve reference to Actor 'source'. (line : 3 column : 27)
ERROR:Couldn't resolve reference to Actor 'disabled'. (line : 3 column : 46)
ERROR:Couldn't resolve reference to Actor 'wants'. (line : 3 column : 73)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 67)
ERROR:Couldn't resolve reference to Actor 'edit'. (line : 3 column : 82)
ERROR:Couldn't resolve reference to Actor 'exchange'. (line : 3 column : 92)

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
Not precise verb: 1
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 90

Progressbar: ![90%](https://progress-bar.dev/90)

            

### Final Score
Final_score = 72.0

Progressbar: ![72.0%](https://progress-bar.dev/72.0)

