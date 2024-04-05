

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:07:45
* UniqueID: d43b5c9f-8228-4f9f-b3b0-9375d2e9530b
* Gherkinscenario name: Gherkinscenario 15: Displaying themed shop homepage_Incorrect_
* LLM-temperature: 0.2

        

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
UserA should see a homepage from that theme should While UserA visit this channel's homepage UserA
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'should' (line : 3 column : 7)
ERROR:missing '.' at 'see' (line : 3 column : 14)
ERROR:no viable alternative at input 'a' (line : 3 column : 18)
ERROR:missing '.' at 'homepage' (line : 3 column : 20)
ERROR:no viable alternative at input 'from' (line : 3 column : 29)
ERROR:no viable alternative at input 'theme' (line : 3 column : 39)
ERROR:no viable alternative at input 'should' (line : 3 column : 45)
ERROR:missing '.' at 'While' (line : 3 column : 52)
ERROR:no viable alternative at input 'this' (line : 3 column : 70)
ERROR:no viable alternative at input 'channel' (line : 3 column : 75)
ERROR:mismatched character '<EOF>' expecting ''' (line : 3 column : 82)
ERROR:Couldn't resolve reference to Actor 'see'. (line : 3 column : 14)
ERROR:Couldn't resolve reference to Actor 'homepage'. (line : 3 column : 20)
ERROR:Couldn't resolve reference to Actor 'theme'. (line : 3 column : 39)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'visit'. (line : 3 column : 64)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 58)
ERROR:Couldn't resolve reference to Actor 'this'. (line : 3 column : 70)

```
### DSL-Rimay Score
DSL_Score: 67

Progressbar: ![67%](https://progress-bar.dev/67)

            


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
Final_score = 71.0

Progressbar: ![71.0%](https://progress-bar.dev/71.0)

