

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__13:55:49
* UniqueID: f513b7fb-f65f-4ced-b274-1bbb3b68df85
* Gherkinscenario name: Gherkinscenario 12: Changing the currency of my cart
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
While UserA has product "The Pug Mug" in the cart   When UserA switches to the "EUR" currency   UserA   must   the grand total value should be "€6.82"
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:mismatched input 'in' expecting ',' (line : 3 column : 39)
ERROR:missing '.' at 'the' (line : 3 column : 42)
ERROR:no viable alternative at input 'When' (line : 3 column : 53)
ERROR:missing '.' at 'UserA' (line : 3 column : 58)
ERROR:no viable alternative at input 'switches' (line : 3 column : 64)
ERROR:missing '.' at 'the' (line : 3 column : 76)
ERROR:extraneous input '"EUR"' expecting RULE_ID (line : 3 column : 80)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 97)
ERROR:no viable alternative at input 'total' (line : 3 column : 122)
ERROR:missing '.' at 'should' (line : 3 column : 134)
ERROR:no viable alternative at input 'be' (line : 3 column : 141)
ERROR:mismatched input '<EOF>' expecting '.' (line : 3 column : 144)
ERROR:Couldn't resolve reference to Quantifier 'product'. (line : 3 column : 17)
ERROR:Couldn't resolve reference to Actor 'cart'. (line : 3 column : 46)
ERROR:Couldn't resolve reference to Actor 'currency'. (line : 3 column : 86)
ERROR:Couldn't resolve reference to Actor 'grand'. (line : 3 column : 116)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 3 column : 134)

```
### DSL-Rimay Score
DSL_Score: 67

Progressbar: ![67%](https://progress-bar.dev/67)

            


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
Final_score = 86.0

Progressbar: ![86.0%](https://progress-bar.dev/86.0)

