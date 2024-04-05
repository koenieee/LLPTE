

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:05:40
* UniqueID: b949b197-c744-4d6a-a908-a9d6460b15d6
* Gherkinscenario name: Gherkinscenario 14: Displaying default shop homepage_Incorrect_
* LLM-temperature: 0.2

        

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

Rimay CNL definition: $SYSTEM_RESPONSE  $MODAL_VERB      $WHILE_STRUCTURE         $ACTOR      $WHEN_STRUCTURE

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
UserA should not see a homepage from "maverick/meerkat" theme should SystemA While UserA visits this channel's homepage
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'should' (line : 3 column : 7)
ERROR:missing '.' at 'see' (line : 3 column : 18)
ERROR:no viable alternative at input 'a' (line : 3 column : 22)
ERROR:missing '.' at 'homepage' (line : 3 column : 24)
ERROR:no viable alternative at input 'from' (line : 3 column : 33)
ERROR:no viable alternative at input 'theme' (line : 3 column : 57)
ERROR:no viable alternative at input 'should' (line : 3 column : 63)
ERROR:missing '.' at 'SystemA' (line : 3 column : 70)
ERROR:no viable alternative at input 'While' (line : 3 column : 78)
ERROR:missing '.' at 'UserA' (line : 3 column : 84)
ERROR:no viable alternative at input 'visits' (line : 3 column : 90)
ERROR:missing '.' at 'this' (line : 3 column : 97)
ERROR:no viable alternative at input 'channel' (line : 3 column : 102)
ERROR:mismatched character '<EOF>' expecting ''' (line : 3 column : 109)
ERROR:Couldn't resolve reference to Actor 'see'. (line : 3 column : 18)
ERROR:Couldn't resolve reference to Actor 'homepage'. (line : 3 column : 24)
ERROR:Couldn't resolve reference to Actor 'theme'. (line : 3 column : 57)
ERROR:Couldn't resolve reference to Actor 'this'. (line : 3 column : 97)

```
### DSL-Rimay Score
DSL_Score: 66

Progressbar: ![66%](https://progress-bar.dev/66)

            


## Rimay Paska Verification
```
File generated_rimay.csv.csv
Smells found in this document: 
Non-atomic requirement: 0
Incomplete requirement: 0
Incorrect order requirement: 1
Coordination ambiguity: 0
Not requirement: ,0
Incomplete condition: 1
Incomplete system response: 0
Passive voice: 0
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 85

Progressbar: ![85%](https://progress-bar.dev/85)

            

### Final Score
Final_score = 65.5

Progressbar: ![65.5%](https://progress-bar.dev/65.5)

