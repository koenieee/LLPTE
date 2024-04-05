

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:49:54
* UniqueID: bc5a455b-0501-4e39-8daa-2c6087228c2c
* Gherkinscenario name: Gherkinscenario 11: Seeing disabled code field while editing country_Incorrect_
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: SystemA has country "United States"
When: UserA wants to edit this country
Then: the code field should be disabled
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
Given: SystemA has country "United States"
When: UserA wants to edit this country
Then: the code field should be disabled
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
SystemA has country "United States" should be While UserA wants to edit this country
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'has' (line : 3 column : 9)
ERROR:no viable alternative at input 'country' (line : 3 column : 13)
ERROR:no viable alternative at input '"United States"' (line : 3 column : 21)
ERROR:no viable alternative at input 'should' (line : 3 column : 37)
ERROR:no viable alternative at input 'be' (line : 3 column : 44)
ERROR:missing '.' at 'While' (line : 3 column : 47)
ERROR:no viable alternative at input 'to' (line : 3 column : 65)
ERROR:missing ',' at 'edit' (line : 3 column : 68)
ERROR:no viable alternative at input 'this' (line : 3 column : 73)
ERROR:missing '.' at 'country' (line : 3 column : 78)
ERROR:Couldn't resolve reference to Actor 'country'. (line : 3 column : 13)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 3 column : 37)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'wants'. (line : 3 column : 59)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 53)
ERROR:Couldn't resolve reference to Actor 'edit'. (line : 3 column : 68)
ERROR:Couldn't resolve reference to Actor 'country'. (line : 3 column : 78)

```
### DSL-Rimay Score
DSL_Score: 78

Progressbar: ![78%](https://progress-bar.dev/78)

            


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
Final_score = 74.0

Progressbar: ![74.0%](https://progress-bar.dev/74.0)

