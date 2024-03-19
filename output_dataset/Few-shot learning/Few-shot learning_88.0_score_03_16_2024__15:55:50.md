

# LLM Experiment Information
* Prefix:   Few-shot learning
* Datetime: 03_16_2024__15:55:50
* UniqueID: 178ae05d-82ee-41af-8c04-ebffd60e4eb7

        

## Gherkin Input
```
Given: that the account is overdrawn
            And: the card is valid
            When: the customer requests the cash
            Then: ensure the rejection message is displayed
            And: ensure cash isn't dispensed
```
    



## Input prompt, technique: Few-Shot Learning


### Context
The following syntax structure is called Rimay, this is a CNL (Controlled Natural Language):

$ACTOR is for example a thing or a person.
$MODAL_VERB is for example the following word: must and shall.
$TRIGGER is for example a trigger action, something what a system does.
$WHEN_STRUCTURE is the word  'When' followed by the variable defined $TRIGGER.
$SYSTEM_RESPONSE is something that the syst

$ACTOR, $MODAL_VERB and a $SYSTEM_RESPONSE is mandatory in all Rimay requirements.
Replace the variables with the right text according the input acceptance criteria.
In the following order: 

Rimay CNL definition: $WHEN_STRUCTURE   $ACTOR   $MODAL_VERB    $SYSTEM_RESPONSE

really important rule, make only use of the following word list:

This list of variables is important and can be used to formulete Rimay:
Only make use of the following words:

is, are, equal, equals, greater than, less than, has, have, contain, contains, do, does, every, 
before, after, if, and, or, not, of, permit, permits, accept, acepts, allow, allows, is, are, shall, must, 
a, an, the, do, the, following, actions, exclude, excludes, instruct, instructs, 
allow, allows, authorize, authorizes, request, requests, 
start, starts, begin, begins, cancel, cancels, hide, hides, 
restore, restores, compute, computes, publish, publishes, enable, disable, 
enforce, enforces, create, creates, generate, generates, replace, replaces, 
prevent, prevents, download, downloads, aggregate, aggregates, 
interrupt, interrupts, include, includes, store, stores, property, properties, value, values, 
limit, limits, restrict, restricts, reduce, reduces, migrate, migrates, 
add, adds, link, links, neglect, neglects, ignore, ignores, accept, accepts, receive, receives, retrieve, retrieves, 
close, closes, reverse, reverses, insert, inserts, display, displays, show, shows, 
extract, extracts, remove, removes, delete, deletes, deduct, deducts, report, reports, propose, proposes, 
detect, detects, select, selects, unselect, unselects, return, returns, send, sends, forward, forward, pass, passes, export, exports, 
concatenate, concatenates, synchronize, synchronizes, discard, discards, copy, copies, 
convert, converts, change, changes, transform, transforms, update, updates, set, sets, 
use, uses, apply, applies, validate, validates, check, checks, calculate, calculates, recalculate, recalculates
establish, establishes, search, searches, split, splits, stop, stops, finish, finishes
subscribe, subscribes, upload, uploads


Important extra rule: if the word is not defined in the list above, put if between quotes.
DO NOT WRITE ANY OTHER WORDS THAN THE DEFINED WORD LIST!

The following example is a valid Rimay CNL:

When SystemB receives an "email alert" from SystemA, SystemB must send an Instruction to SystemC.

With the usage of the following extra information:
Actors: actor SystemA, actor SystemB, actor SystemC, actor UserX, actor UserA, actor UserC
Classes: class Instruction := description record, class Y

THIS IS NOT VALID RIMAY:
When UserA navigates to the login page, UserA clicks on button, SystemA must refresh the page.

The following example would be valid:
When UserA "navigates to the login page", UserA "clicks on button", SystemA must "refresh the page".
        

### Input Data
Use the following Gherkin acceptance criteria input: 
```
Given: that the account is overdrawn
            And: the card is valid
            When: the customer requests the cash
            Then: ensure the rejection message is displayed
            And: ensure cash isn't dispensed
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only your translated Rimay CNL text and nothing else!


## Rimay Output
```
When the "account" is "overdrawn", the "card" is "valid", the "customer" requests the "cash", the system must "display" the "rejection message" and must "not dispense" the "cash".
``` 
            


## Rimay DSL Verification
```
ERROR:missing RULE_ID at '"account"' (line : 3 column : 10)
ERROR:no viable alternative at input 'is' (line : 3 column : 20)
ERROR:mismatched input '"card"' expecting RULE_ID (line : 3 column : 40)
ERROR:missing '.' at 'the' (line : 3 column : 59)
ERROR:mismatched input '"customer"' expecting RULE_ID (line : 3 column : 63)
ERROR:missing '.' at 'the' (line : 3 column : 83)
ERROR:mismatched input '"cash"' expecting RULE_ID (line : 3 column : 87)
ERROR:missing '.' at 'the' (line : 3 column : 95)
ERROR:no viable alternative at input '"display"' (line : 3 column : 111)
ERROR:missing '.' at 'the' (line : 3 column : 121)
ERROR:mismatched input '"rejection message"' expecting RULE_ID (line : 3 column : 125)
ERROR:missing '.' at 'the' (line : 3 column : 169)
ERROR:mismatched input '"cash"' expecting RULE_ID (line : 3 column : 173)
ERROR:Couldn't resolve reference to Actor 'system'. (line : 3 column : 99)

```
### Score
Score: 80
Progressbar: ![80%](https://progress-bar.dev/80)

            


## Rimay Paska Verification
```
File generated_rimay.csv.csv
Smells found in this document: 
Non-atomic requirement: 1
Incomplete requirement: 0
Incorrect order requirement: 0
Coordination ambiguity: 0
Not requirement: ,0
Incomplete condition: 0
Incomplete system response: 0
Passive voice: 0
Not precise verb: 0
Number Req with smells: 1

```
### Score
Score: 96
Progressbar: ![96%](https://progress-bar.dev/96)

            

Final_score = 88.0
