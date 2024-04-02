

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_02_2024__16:31:28
* UniqueID: dd9e5dea-4851-4655-aa9e-3a16156f0e36
* Scenario name: Scenario 5: Getting verified after clicking the link in the verification message

        

## Gherkin Input
```
Given: a verification email has already been sent to "UserA"
When: UserA tries to verify his account using the link from this email
Then: UserA should be notified that the verification was successful
```
    



## Input prompt, technique: Few-Shot-Learning


### Context
We are translating Gherkin acceptance criteria into Rimay CNL.
For this translation use the followin information:

$ACTOR is for example a thing or a person.
$MODAL_VERB is for  the following word: must or shall.
$TRIGGER is for example a trigger action, something what a system does.

$WHILE_STRUCTURE is the word 'While' followed by the Gherkin Given condition
$WHEN_STRUCTURE is the word  'When' followed by the Gherkin When condition
$SYSTEM_RESPONSE is a combination of the Actors and the Gherkin Then condition.

$ACTOR, $MODAL_VERB and a $SYSTEM_RESPONSE is mandatory in all Rimay requirements.
Replace the variables with the right text according the input acceptance criteria.
In the following order: 

Rimay CNL definition: $WHILE_STRUCTURE $WHEN_STRUCTURE   $ACTOR   $MODAL_VERB    $SYSTEM_RESPONSE

The following example is a valid Rimay CNL:

When SystemB receives an "email alert" from SystemA, SystemB must send an Instruction to SystemC.

With the usage of the following extra information:
Actors: actor SystemA, actor SystemB, actor SystemC, actor UserX, actor UserA, actor UserC

THIS IS NOT VALID RIMAY:
When UserA navigates to the login page, UserA clicks on button, SystemA must refresh the page.

The following example would be valid:
When UserA "navigates to the login page", UserA "clicks on button", SystemA must "refresh the page".
        

### Input Data
Use the following Gherkin acceptance criteria input: 
```
Given: a verification email has already been sent to "UserA"
When: UserA tries to verify his account using the link from this email
Then: UserA should be notified that the verification was successful
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only your translated Rimay CNL text and nothing else!


## Rimay Output
```
While a verification email has already been sent to UserA When UserA tries to verify his account using the link from this email UserA must be notified that the verification was successful.
``` 
            

### Researcher score
Researcher_score = 0.95


## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'email' (line : 3 column : 22)
ERROR:no viable alternative at input 'has' (line : 3 column : 28)
ERROR:no viable alternative at input 'already' (line : 3 column : 32)
ERROR:no viable alternative at input 'been' (line : 3 column : 40)
ERROR:missing '.' at 'sent' (line : 3 column : 45)
ERROR:no viable alternative at input 'to' (line : 3 column : 50)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 53)
ERROR:no viable alternative at input 'When' (line : 3 column : 59)
ERROR:missing '.' at 'UserA' (line : 3 column : 64)
ERROR:no viable alternative at input 'tries' (line : 3 column : 70)
ERROR:missing '.' at 'verify' (line : 3 column : 79)
ERROR:no viable alternative at input 'his' (line : 3 column : 86)
ERROR:missing '.' at 'account' (line : 3 column : 90)
ERROR:no viable alternative at input 'using' (line : 3 column : 98)
ERROR:no viable alternative at input 'the' (line : 3 column : 104)
ERROR:mismatched input 'link' expecting RULE_ID (line : 3 column : 108)
ERROR:missing '.' at 'this' (line : 3 column : 118)
ERROR:no viable alternative at input 'email' (line : 3 column : 123)
ERROR:missing '.' at 'UserA' (line : 3 column : 129)
ERROR:no viable alternative at input 'be' (line : 3 column : 140)
ERROR:no viable alternative at input 'notified' (line : 3 column : 143)
ERROR:missing '.' at 'the' (line : 3 column : 157)
ERROR:no viable alternative at input 'was' (line : 3 column : 174)
ERROR:extraneous input 'successful' expecting '.' (line : 3 column : 178)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'verification'. (line : 3 column : 9)
ERROR:Couldn't resolve reference to Actor 'email'. (line : 3 column : 22)
ERROR:Couldn't resolve reference to Actor 'already'. (line : 3 column : 32)
ERROR:Couldn't resolve reference to Actor 'sent'. (line : 3 column : 45)
ERROR:Couldn't resolve reference to Actor 'verify'. (line : 3 column : 79)
ERROR:Couldn't resolve reference to Actor 'account'. (line : 3 column : 90)
ERROR:Couldn't resolve reference to Actor 'this'. (line : 3 column : 118)
ERROR:Couldn't resolve reference to Actor 'be'. (line : 3 column : 140)
ERROR:Couldn't resolve reference to Actor 'verification'. (line : 3 column : 161)

```
### DSL-Rimay Score
DSL_Score: 61
Progressbar: ![61%](https://progress-bar.dev/61)

            


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
Final_score = 64.6
