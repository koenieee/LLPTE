

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:59:36
* UniqueID: 88c2e699-3919-4d8e-9887-d1230d5669a3
* Gherkinscenario name: Gherkinscenario 15: Displaying themed shop homepage
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: channel "United States" uses "maverick/meerkat" theme
When: UserA visit this channel's homepage
Then: UserA should see a homepage from that theme
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
Given: channel "United States" uses "maverick/meerkat" theme
When: UserA visit this channel's homepage
Then: UserA should see a homepage from that theme
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
While channel "United States" uses "maverick/meerkat" theme When UserA visits this channel's homepage UserA must see a homepage from that theme
``` 
            

### Researcher score
Researcher_score = 10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'uses' (line : 3 column : 7)
ERROR:no viable alternative at input '"United States"' (line : 3 column : 15)
ERROR:missing '.' at 'theme' (line : 3 column : 55)
ERROR:no viable alternative at input 'When' (line : 3 column : 61)
ERROR:missing '.' at 'UserA' (line : 3 column : 66)
ERROR:no viable alternative at input 'visits' (line : 3 column : 72)
ERROR:missing '.' at 'this' (line : 3 column : 79)
ERROR:no viable alternative at input 'channel' (line : 3 column : 84)
ERROR:mismatched character '<EOF>' expecting ''' (line : 3 column : 91)
ERROR:Couldn't resolve reference to Actor 'channel'. (line : 3 column : 7)
ERROR:Couldn't resolve reference to Actor 'theme'. (line : 3 column : 55)
ERROR:Couldn't resolve reference to Actor 'this'. (line : 3 column : 79)

```
### DSL-Rimay Score
DSL_Score: 72

Progressbar: ![72%](https://progress-bar.dev/72)

            


## Rimay Paska Verification
```
File generated_rimay.csv.csv
Smells found in this document: 
Non-atomic requirement: 0
Incomplete requirement: 0
Incorrect order requirement: 0
Coordination ambiguity: 0
Not requirement: ,0
Incomplete condition: 1
Incomplete system response: 0
Passive voice: 0
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 90

Progressbar: ![90%](https://progress-bar.dev/90)

            

### Final Score
Final_score = 91.0

Progressbar: ![91.0%](https://progress-bar.dev/91.0)

