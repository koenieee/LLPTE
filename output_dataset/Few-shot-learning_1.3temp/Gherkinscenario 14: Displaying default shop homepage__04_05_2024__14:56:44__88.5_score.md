

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:56:44
* UniqueID: 7c7978f9-16a2-4ce3-819b-cdb19a275fac
* Gherkinscenario name: Gherkinscenario 14: Displaying default shop homepage
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: channel "United States" does not use any theme
When: UserA visits this channel's homepage
Then: UserA should not see a homepage from "maverick/meerkat" theme
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
Given: channel "United States" does not use any theme
When: UserA visits this channel's homepage
Then: UserA should not see a homepage from "maverick/meerkat" theme
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
While channel "United States" does not use any theme When UserA visits this channel's homepage UserA must not see a homepage from "maverick/meerkat" theme
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'use' (line : 3 column : 7)
ERROR:no viable alternative at input '"United States"' (line : 3 column : 15)
ERROR:missing '.' at 'When' (line : 3 column : 54)
ERROR:no viable alternative at input 'this' (line : 3 column : 72)
ERROR:no viable alternative at input 'channel' (line : 3 column : 77)
ERROR:mismatched character '<EOF>' expecting ''' (line : 3 column : 84)
ERROR:Couldn't resolve reference to Actor 'channel'. (line : 3 column : 7)
ERROR:Couldn't resolve reference to ClassOrLabelOrProperty 'theme'. (line : 3 column : 48)
ERROR:Couldn't resolve reference to Quantifier 'any'. (line : 3 column : 44)
ERROR:Couldn't resolve reference to Actor 'visits'. (line : 3 column : 65)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 59)
ERROR:Couldn't resolve reference to Actor 'this'. (line : 3 column : 72)

```
### DSL-Rimay Score
DSL_Score: 72

Progressbar: ![72%](https://progress-bar.dev/72)

            


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
Final_score = 88.5

Progressbar: ![88.5%](https://progress-bar.dev/88.5)

