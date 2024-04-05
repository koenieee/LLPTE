

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:58:20
* UniqueID: 506a6695-46d0-41fa-acbd-cfe9012ae716
* Gherkinscenario name: Gherkinscenario 14: Displaying default shop homepage_Incorrect_
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
UserA should visit this channel's homepage should not see a homepage from "maverick/meerkat" theme.
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'should' (line : 3 column : 7)
ERROR:missing '.' at 'visit' (line : 3 column : 14)
ERROR:no viable alternative at input 'this' (line : 3 column : 20)
ERROR:missing '.' at 'channel' (line : 3 column : 25)
ERROR:mismatched character '<EOF>' expecting ''' (line : 3 column : 32)
ERROR:Couldn't resolve reference to Actor 'visit'. (line : 3 column : 14)
ERROR:Couldn't resolve reference to Actor 'channel'. (line : 3 column : 25)

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
Final_score = 78.5

Progressbar: ![78.5%](https://progress-bar.dev/78.5)

