

# LLM Experiment Information
* Prefix:   Chain-of-thought
* Datetime: 04_08_2024__21:52:28
* UniqueID: 6c827e1d-26a2-4a5b-b6f0-12e1fec53818
* Gherkinscenario name: Gherkinscenario 17: Seeing the unpaid order in the list_Incorrect_
* LLM-temperature: 0.2

        

## Gherkin Input
```
Given: UserA logged in as "john@example.com"
When: UserA views order history
Then: UserA should sees one order with total of $29.99
```
    



## Input prompt, technique: Chain-of-Thought


Learn from the following example, the output information for the CNL Rimay is: 
This part is the start of the example you have to learn from:

The input information is as follows: 

Gherkin input 1:
Scenario: Create an Order
Given an Order of type Subscription_Order does not exist in OI of type Order_Issuer 
When OI Create Order, 
Then Order exists in OI 
And the property settlement_method of Order is equal to FOP


Rimay output 1:
When the Order_Issuer (OI ) executes  a Subscription_Order, 
then the  is set to FOP.


Gherkin input 2:
Given: a verification email has already been sent to "operator"
When: operator tries to verify his account using the link from this email
Then: operator should be notified that the verification was successful

Rimay output 2:
When operator validates "email address" 
then system must notify operator.  
 

Gherkin input 3: 
visitor is editing the address of "Fletcher Ren"
Then: visitor should still be on the "Fletcher Ren" address edit page


Rimay output 3:
While visitor is "Ren" 
then website must show something.


Ending example of translation from Gherkin into Rimay.


### Input Data
Use the following Gherkin acceptance criteria input: 
```
Given: UserA logged in as "john@example.com"
When: UserA views order history
Then: UserA should sees one order with total of $29.99
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
Given UserA is logged in as "john@example.com"
When UserA checks order history
Then UserA must see one order with a total of $29.99.
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'UserA' (line : 3 column : 7)
ERROR:missing '.' at 'logged' (line : 3 column : 16)
ERROR:no viable alternative at input 'in' (line : 3 column : 23)
ERROR:no viable alternative at input 'When' (line : 4 column : 1)
ERROR:mismatched input 'Then' expecting 'by' (line : 5 column : 1)
ERROR:no viable alternative at input 'must' (line : 5 column : 12)
ERROR:no viable alternative at input 'see' (line : 5 column : 17)
ERROR:no viable alternative at input 'one' (line : 5 column : 21)
ERROR:missing '.' at 'order' (line : 5 column : 25)
ERROR:no viable alternative at input 'with' (line : 5 column : 31)
ERROR:no viable alternative at input 'a' (line : 5 column : 36)
ERROR:no viable alternative at input 'of' (line : 5 column : 44)
ERROR:no viable alternative at input '.' (line : 5 column : 50)
ERROR:missing EOF at '99' (line : 5 column : 51)
ERROR:Couldn't resolve reference to Actor 'Given'. (line : 3 column : 1)
ERROR:Couldn't resolve reference to Actor 'logged'. (line : 3 column : 16)
ERROR:Couldn't resolve reference to Quantifier 'order'. (line : 4 column : 19)
ERROR:Couldn't resolve reference to ClassOrLabel 'history'. (line : 4 column : 25)
ERROR:Couldn't resolve reference to Quantifier 'Then'. (line : 5 column : 1)
ERROR:Couldn't resolve reference to Actor 'see'. (line : 5 column : 17)
ERROR:Couldn't resolve reference to Actor 'order'. (line : 5 column : 25)
ERROR:Couldn't resolve reference to Actor 'total'. (line : 5 column : 38)

```
### DSL-Rimay Score
DSL_Score: 62

Progressbar: ![62%](https://progress-bar.dev/62)

            


## Rimay Paska Verification
```
File generated_rimay.csv.csv
Smells found in this document: 
Non-atomic requirement: 0
Incomplete requirement: 0
Incorrect order requirement: 0
Coordination ambiguity: 0
Not requirement: ,1
Incomplete condition: 0
Incomplete system response: 0
Passive voice: 0
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 80

Progressbar: ![80%](https://progress-bar.dev/80)

            

### Final Score
Final_score = 61.0

Progressbar: ![61.0%](https://progress-bar.dev/61.0)

