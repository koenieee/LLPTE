

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:33:56
* UniqueID: c987e803-7214-4ede-bc11-4863e9a39475
* Gherkinscenario name: Gherkinscenario 4: User presses button._Incorrect_
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: UserA navigates to the login page
When: UserA clicks on button
Then: SystemA refreshes page
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
Given: UserA navigates to the login page
When: UserA clicks on button
Then: SystemA refreshes page
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
SystemA refreshes page should When UserA navigates to the login page While UserA clicks on button
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'refreshes' (line : 3 column : 9)
ERROR:missing '.' at 'page' (line : 3 column : 19)
ERROR:no viable alternative at input 'should' (line : 3 column : 24)
ERROR:missing '.' at 'When' (line : 3 column : 31)
ERROR:no viable alternative at input 'to' (line : 3 column : 52)
ERROR:missing ',' at 'the' (line : 3 column : 55)
ERROR:no viable alternative at input 'page' (line : 3 column : 65)
ERROR:missing '.' at 'While' (line : 3 column : 70)
ERROR:no viable alternative at input 'clicks' (line : 3 column : 76)
ERROR:no viable alternative at input 'clicks' (line : 3 column : 82)
ERROR:no viable alternative at input 'button' (line : 3 column : 92)
ERROR:Couldn't resolve reference to Actor 'page'. (line : 3 column : 19)
ERROR:Couldn't resolve reference to Actor 'navigates'. (line : 3 column : 42)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 36)
ERROR:Couldn't resolve reference to Actor 'login'. (line : 3 column : 59)
ERROR:Couldn't resolve reference to Actor 'button'. (line : 3 column : 92)

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
Incomplete system response: 1
Passive voice: 0
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 80

Progressbar: ![80%](https://progress-bar.dev/80)

            

### Final Score
Final_score = 69.0

Progressbar: ![69.0%](https://progress-bar.dev/69.0)

