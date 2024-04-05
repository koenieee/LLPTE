

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__15:05:54
* UniqueID: 17e38e8c-2480-4532-bb17-b968cabf6938
* Gherkinscenario name: Gherkinscenario 18: Being unable to change currencies
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
While the exchange rate of "US Dollar" to "British Pound" is 1.30 When UserA UserA must see that the source currency is disabled
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'rate' (line : 3 column : 20)
ERROR:no viable alternative at input 'of' (line : 3 column : 25)
ERROR:no viable alternative at input '.' (line : 3 column : 63)
ERROR:missing EOF at '30' (line : 3 column : 64)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'exchange'. (line : 3 column : 11)
ERROR:Couldn't resolve reference to Actor 'rate'. (line : 3 column : 20)

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

