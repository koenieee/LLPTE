
### Input prompt, technique: Few-Shot Learning

```


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
Use the following Gherkin acceptance criteria input data: 
Given: UserA navigates to the login page
When: UserA clicks on button
Then: SystemA refreshes page

### Question:
Can you translate the inputdata above into the specified language Rimay CNL?

### Output indicator
Output only your translated Rimay CNL text and nothing else!

```
### Output result 
When UserA "navigates to the login page", UserA "clicks on button", SystemA must "refresh the page".

### Input prompt, technique: Chain of Thought

```


        Learn from the following example, the output information for the CNL Rimay is: 
        This part is the start of the example you have to learn from:

        The input information is as follows: 

        Acceptance Criteria 1 in Gherkin, input:
        Gherkin:
        Scenario: Create an Order
        Given an Order of type Subscription_Order does not exist in OI of type Order_Issuer 
        When OI Create Order, 
        Then Order exists in OI 
        And the property settlement_method of Order is equal to FOP


        Rimay output 1:
        When the Order_Issuer (OI ) executes Create a Subscription_Order, if the Order does not exist, then the Order is created and its settlement_method is set to FOP.

        Rimay uses the following structure:
        When the? Actor <Action> (every "Frequency")? ,|then the? Actor must <Action> (every "Text")?.

        Ending for example


        Translate the following input acceptance criteria Gherkin, according to the example above, to Rimay:


        

### Input Data
Use the following Gherkin acceptance criteria input data: 
Given: UserA navigates to the login page
When: UserA clicks on button
Then: SystemA refreshes page

### Question:
Can you translate the inputdata above into the specified language Rimay CNL?

### Output indicator
Output only your translated Rimay CNL text and nothing else!

```
### Output result 
Given UserA navigates to the login page, when UserA clicks on button, then SystemA refreshes page.

### Input prompt, technique: Role Play

```


        Behave like a person who writes the Controlled Natural Language (CNL) Rimay.
        Rimay is a language that is defined in different components. 
        For now we only highlight the following components:

        Mandatory:

        $ACTOR = SystemA
        $MODAL_VERB = should, can, could, might, will
        $SYSTEM_RESPONSE = SYSTEM_RESPONSE_EXPRESSION | RESPONSE_BLOCK_ITEMIZED 
        $SYSTEM_RESPONSE_EXPRESSION: ATOMIC_SYSTEM_RESPONSE ((,|, and|, or|and|or)? ATOMIC_SYSTEM_RESPONSE)* ATOMIC_SYSTEM_RESPONSE: ACTION_PHRASE (every TEXT )? RESPONSE_BLOCK_ITEMIZED: do the following actions (in sequence)? : BULLET ATOMIC_SYSTEM_RESPONSE ((,|, and|, or|and|or)? BULLET ATOMIC_SYSTEM_RESPONSE)*
        Optional:
        $WHEN_STRUCTURE : When TRIGGER

        Use for ACTOR for example SystemA and use for MODAL_VERB for example the following words: should, can, could, might, will


        $ACTOR, $MODAL_VERB and $SYSTEM_RESPONSE is mandatory in all Rimay requirements.

        Rimay CNL: $WHEN_STRUCTURE  $ACTOR   $MODAL_VERB     $SYSTEM_RESPONSE

        Now I want you to answer as the person who writes Rimay to translate this acceptance criteria into Rimay

        

### Input Data
Use the following Gherkin acceptance criteria input data: 
Given: UserA navigates to the login page
When: UserA clicks on button
Then: SystemA refreshes page

### Question:
Can you translate the inputdata above into the specified language Rimay CNL?

### Output indicator
Output only your translated Rimay CNL text and nothing else!

```
### Output result 
$ACTOR SystemA $MODAL_VERB should $SYSTEM_RESPONSE SystemA refreshes page

### Input prompt, technique: Role Play

```


        Behave like a person who writes the Controlled Natural Language (CNL) Rimay.
        Rimay is a language that is defined in different components. 
        For now we only highlight the following components:

        Mandatory:

        $ACTOR = SystemA
        $MODAL_VERB = should, can, could, might, will
        $SYSTEM_RESPONSE = SYSTEM_RESPONSE_EXPRESSION | RESPONSE_BLOCK_ITEMIZED 
        $SYSTEM_RESPONSE_EXPRESSION: ATOMIC_SYSTEM_RESPONSE ((,|, and|, or|and|or)? ATOMIC_SYSTEM_RESPONSE)* ATOMIC_SYSTEM_RESPONSE: ACTION_PHRASE (every TEXT )? RESPONSE_BLOCK_ITEMIZED: do the following actions (in sequence)? : BULLET ATOMIC_SYSTEM_RESPONSE ((,|, and|, or|and|or)? BULLET ATOMIC_SYSTEM_RESPONSE)*
        Optional:
        $WHEN_STRUCTURE : When TRIGGER

        Use for ACTOR for example SystemA and use for MODAL_VERB for example the following words: should, can, could, might, will


        $ACTOR, $MODAL_VERB and $SYSTEM_RESPONSE is mandatory in all Rimay requirements.

        Rimay CNL: $WHEN_STRUCTURE  $ACTOR   $MODAL_VERB     $SYSTEM_RESPONSE

        Now I want you to answer as the person who writes Rimay to translate this acceptance criteria into Rimay

        

### Input Data
Use the following Gherkin acceptance criteria input data: 
Given: that the account is overdrawn
When: the customer requests the cash
Then: ensure the rejection message is displayed

### Question:
Can you translate the inputdata above into the specified language Rimay CNL?

### Output indicator
Output only your translated Rimay CNL text and nothing else!

```
### Output result 
$ACTOR SystemA should do the following actions in sequence: 
- ensure the rejection message is displayed

### Input prompt, technique: Few-Shot Learning

```


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
Use the following Gherkin acceptance criteria input data: 
Given: that the account is overdrawn
When: the customer requests the cash
Then: ensure the rejection message is displayed

### Question:
Can you translate the inputdata above into the specified language Rimay CNL?

### Output indicator
Output only your translated Rimay CNL text and nothing else!

```
### Output result 
When the customer requests the cash, the account must display the rejection message.

### Input prompt, technique: Few-Shot Learning

```


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
Use the following Gherkin acceptance criteria input data: 
Given: UserA navigates to the login page
When: UserA clicks on button
Then: SystemA refreshes page

### Question:
Can you translate the inputdata above into the specified language Rimay CNL?

### Output indicator
Output only your translated Rimay CNL text and nothing else!

```
### Output result 
When UserA navigates to the login page, UserA clicks on button, SystemA must refresh the page.

### Input prompt, technique: Few-Shot Learning

```


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
Use the following Gherkin acceptance criteria input data: 
Given: UserA navigates to the login page
When: UserA clicks on button
Then: SystemA refreshes page

### Question:
Can you translate the inputdata above into the specified language Rimay CNL?

### Output indicator
Output only your translated Rimay CNL text and nothing else!

```
### Output result 
When UserA navigates to the login page, UserA clicks on button, SystemA must refresh the page.

### Input prompt, technique: Few-Shot Learning

```


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
Use the following Gherkin acceptance criteria input data: 
Given: UserA navigates to the login page
When: UserA clicks on button
Then: SystemA refreshes page

### Question:
Can you translate the inputdata above into the specified language Rimay CNL?

### Output indicator
Output only your translated Rimay CNL text and nothing else!

```
### Output result 
When UserA navigates to the login page, UserA clicks on button, SystemA must refresh the page.

### Input prompt, technique: Few-Shot Learning

```


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
Use the following Gherkin acceptance criteria input data: 
Given: UserA navigates to the login page
When: UserA clicks on button
Then: SystemA refreshes page

### Question:
Can you translate the inputdata above into the specified language Rimay CNL?

### Output indicator
Output only your translated Rimay CNL text and nothing else!

```
### Output result 
When UserA navigates to the login page, UserA clicks on button, SystemA must refresh the page.

### Input prompt, technique: Chain of Thought

```


        Learn from the following example, the output information for the CNL Rimay is: 
        This part is the start of the example you have to learn from:

        The input information is as follows: 

        Acceptance Criteria 1 in Gherkin, input:
        Gherkin:
        Scenario: Create an Order
        Given an Order of type Subscription_Order does not exist in OI of type Order_Issuer 
        When OI Create Order, 
        Then Order exists in OI 
        And the property settlement_method of Order is equal to FOP


        Rimay output 1:
        When the Order_Issuer (OI ) executes Create a Subscription_Order, if the Order does not exist, then the Order is created and its settlement_method is set to FOP.

        Rimay uses the following structure:
        When the? Actor <Action> (every "Frequency")? ,|then the? Actor must <Action> (every "Text")?.

        Ending for example


        Translate the following input acceptance criteria Gherkin, according to the example above, to Rimay:


        

### Input Data
Use the following Gherkin acceptance criteria input data: 
Given: UserA navigates to the login page
When: UserA clicks on button
Then: SystemA refreshes page

### Question:
Can you translate the inputdata above into the specified language Rimay CNL?

### Output indicator
Output only your translated Rimay CNL text and nothing else!

```
### Output result 
Given the UserA navigates to the login page, when the UserA clicks on the button, then the SystemA refreshes the page.
