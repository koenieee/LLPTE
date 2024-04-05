

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:12:44
* UniqueID: d3c4b60e-3b50-49d9-9274-13604d78ff04
* Gherkinscenario name: Gherkinscenario 18: Being unable to change currencies
* LLM-temperature: 0.2

        

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
When UserA wants to edit the exchange rate of "US Dollar" to "British Pound", UserA must see that the source currency is disabled.
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'to' (line : 3 column : 18)
ERROR:missing ',' at 'edit' (line : 3 column : 21)
ERROR:no viable alternative at input 'the' (line : 3 column : 26)
ERROR:missing '.' at 'exchange' (line : 3 column : 30)
ERROR:no viable alternative at input 'rate' (line : 3 column : 39)
ERROR:missing '.' at 'UserA' (line : 3 column : 79)
ERROR:no viable alternative at input 'see' (line : 3 column : 90)
ERROR:no viable alternative at input 'that' (line : 3 column : 94)
ERROR:no viable alternative at input 'the' (line : 3 column : 99)
ERROR:no viable alternative at input 'currency' (line : 3 column : 110)
ERROR:extraneous input 'disabled' expecting '.' (line : 3 column : 122)
ERROR:Couldn't resolve reference to Actor 'wants'. (line : 3 column : 12)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 6)
ERROR:Couldn't resolve reference to Actor 'edit'. (line : 3 column : 21)
ERROR:Couldn't resolve reference to Actor 'exchange'. (line : 3 column : 30)
ERROR:Couldn't resolve reference to Actor 'see'. (line : 3 column : 90)
ERROR:Couldn't resolve reference to Actor 'source'. (line : 3 column : 103)

```
### DSL-Rimay Score
DSL_Score: 77

Progressbar: ![77%](https://progress-bar.dev/77)

            


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
Final_score = 100

Progressbar: ![100%](https://progress-bar.dev/100)

