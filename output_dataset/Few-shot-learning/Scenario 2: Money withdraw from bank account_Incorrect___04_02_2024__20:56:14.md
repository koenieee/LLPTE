

# LLM Experiment Information
* Prefix:   Few-shot-learning
* Datetime: 04_02_2024__20:56:14
* UniqueID: 955e295b-55f9-45f0-b499-27e773527c84
* Scenario name: Scenario 2: Money withdraw from bank account_Incorrect_

        

## Gherkin Input
```
Given: UserA bank account is in credit
When: UserA attempts to withdraw an amount less than UserA card's limit
Then: the withdrawal should be complete without errors or warnings
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

Rimay CNL definition: $WHILE_STRUCTURE      $WHEN_STRUCTURE   $ACTOR   $MODAL_VERB    $SYSTEM_RESPONSE

The following example is a valid Rimay CNL:

When SystemB receives an "email alert" from SystemA, SystemB must send an Instruction to SystemC.

With the usage of the following extra information:
Actors: actor SystemA, actor SystemB, actor SystemC, actor UserX, actor UserA, actor UserC


        

### Question:
Given: UserA bank account is in credit
When: UserA attempts to withdraw an amount less than UserA card's limit
Then: the withdrawal should be complete without errors or warnings

Can you write a random story from 20 words?




## Rimay Output
```
UserA's bank account had enough funds. When UserA withdrew less than the card limit, the transaction completed smoothly.
``` 
            
