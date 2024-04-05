

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_05_2024__14:43:43
* UniqueID: 83374f34-15f4-4e37-a986-c0965cb51de1
* Gherkinscenario name: Gherkinscenario 9: Resending the verification email as a logged in user
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: UserA is logged in as "valkyrie@cain.com"
When: UserA resends the verification email
Then: UserA should be notified that the verification email has been sent
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
Given: UserA is logged in as "valkyrie@cain.com"
When: UserA resends the verification email
Then: UserA should be notified that the verification email has been sent
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
When UserA is logged in as "valkyrie@cain.com", UserA must resend the verification email. UserA should be notified that the verification email has been sent.
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'is' (line : 3 column : 12)
ERROR:missing ',' at 'logged' (line : 3 column : 15)
ERROR:no viable alternative at input 'in' (line : 3 column : 22)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 49)
ERROR:no viable alternative at input 'resend' (line : 3 column : 60)
ERROR:no viable alternative at input 'the' (line : 3 column : 67)
ERROR:missing '.' at 'verification' (line : 3 column : 71)
ERROR:no viable alternative at input 'email' (line : 3 column : 84)
ERROR:no viable alternative at input 'should' (line : 3 column : 97)
ERROR:missing '.' at 'be' (line : 3 column : 104)
ERROR:no viable alternative at input 'notified' (line : 3 column : 107)
ERROR:missing '.' at 'the' (line : 3 column : 121)
ERROR:no viable alternative at input 'email' (line : 3 column : 138)
ERROR:missing '.' at 'been' (line : 3 column : 148)
ERROR:no viable alternative at input 'sent' (line : 3 column : 153)
ERROR:Couldn't resolve reference to Actor 'logged'. (line : 3 column : 15)
ERROR:Couldn't resolve reference to Actor 'resend'. (line : 3 column : 60)
ERROR:Couldn't resolve reference to Actor 'verification'. (line : 3 column : 71)
ERROR:Couldn't resolve reference to Actor 'be'. (line : 3 column : 104)
ERROR:Couldn't resolve reference to Actor 'verification'. (line : 3 column : 125)
ERROR:Couldn't resolve reference to Actor 'been'. (line : 3 column : 148)

```
### DSL-Rimay Score
DSL_Score: 73

Progressbar: ![73%](https://progress-bar.dev/73)

            


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
Passive voice: 1
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 95

Progressbar: ![95%](https://progress-bar.dev/95)

            

### Final Score
Final_score = 99.0

Progressbar: ![99.0%](https://progress-bar.dev/99.0)

