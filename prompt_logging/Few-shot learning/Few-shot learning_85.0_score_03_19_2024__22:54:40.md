

# LLM Experiment Information
* Prefix:   Few-shot learning
* Datetime: 03_19_2024__22:54:40
* UniqueID: 083e8c75-643c-4688-a16a-0dd018d10e41

        

## Gherkin Input
```
Given: I am editing the address of "Fletcher Ren"
When: I remove the street
Then: I should still be on the "Fletcher Ren" address edit page
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
Given: I am editing the address of "Fletcher Ren"
When: I remove the street
Then: I should still be on the "Fletcher Ren" address edit page
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only your translated Rimay CNL text and nothing else!


## Rimay Output
```
When User "I" edits the address of "Fletcher Ren", User "I" removes the street, User "I" should still be on the "Fletcher Ren" address edit page.
``` 
            


## Rimay DSL Verification
```
ERROR:no viable alternative at input 'edits' (line : 3 column : 15)
ERROR:no viable alternative at input 'the' (line : 3 column : 21)
ERROR:missing '.' at 'address' (line : 3 column : 25)
ERROR:no viable alternative at input 'of' (line : 3 column : 33)
ERROR:no viable alternative at input 'User' (line : 3 column : 52)
ERROR:no viable alternative at input '"I"' (line : 3 column : 57)
ERROR:mismatched input 'User' expecting 'or' (line : 3 column : 81)
ERROR:no viable alternative at input '"I"' (line : 3 column : 86)
ERROR:no viable alternative at input 'should' (line : 3 column : 90)
ERROR:no viable alternative at input 'still' (line : 3 column : 97)
ERROR:missing '.' at 'be' (line : 3 column : 103)
ERROR:no viable alternative at input 'on' (line : 3 column : 106)
ERROR:no viable alternative at input 'the' (line : 3 column : 109)
ERROR:extraneous input '"Fletcher Ren"' expecting RULE_ID (line : 3 column : 113)
ERROR:no viable alternative at input 'edit' (line : 3 column : 136)
ERROR:Couldn't resolve reference to Actor 'User'. (line : 3 column : 6)
ERROR:Couldn't resolve reference to Actor 'edits'. (line : 3 column : 15)
ERROR:Couldn't resolve reference to Actor 'address'. (line : 3 column : 25)
ERROR:Couldn't resolve reference to Actor 'User'. (line : 3 column : 52)
ERROR:Couldn't resolve reference to PropertyOrLabel 'street'. (line : 3 column : 73)
ERROR:Couldn't resolve reference to Actor 'User'. (line : 3 column : 81)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 3 column : 90)
ERROR:Couldn't resolve reference to Actor 'be'. (line : 3 column : 103)
ERROR:Couldn't resolve reference to Actor 'address'. (line : 3 column : 128)

```
### Score
Score: 70
Progressbar: ![70%](https://progress-bar.dev/70)

            


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
### Score
Score: 100
Progressbar: ![100%](https://progress-bar.dev/100)

            

### Final Score
Final_score = 85.0
