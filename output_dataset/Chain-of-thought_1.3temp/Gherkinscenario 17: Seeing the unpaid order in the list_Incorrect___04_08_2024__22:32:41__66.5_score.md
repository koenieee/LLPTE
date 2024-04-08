

# LLM Experiment Information
* Prefix:   Chain-of-thought
* Datetime: 04_08_2024__22:32:41
* UniqueID: 7bc3fd43-4f23-4e14-aa46-e766ff2d8934
* Gherkinscenario name: Gherkinscenario 17: Seeing the unpaid order in the list_Incorrect_
* LLM-temperature: 1.3

        

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
Given that "john@example.com" is authenticated as UserA  
When UserA navigates to order history  
Then UserA should see one order with a total of $29.99
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'that' (line : 3 column : 7)
ERROR:no viable alternative at input 'authenticated' (line : 3 column : 34)
ERROR:no viable alternative at input 'as' (line : 3 column : 48)
ERROR:no viable alternative at input 'UserA' (line : 3 column : 51)
ERROR:no viable alternative at input 'When' (line : 4 column : 1)
ERROR:missing '.' at 'UserA' (line : 4 column : 6)
ERROR:no viable alternative at input 'navigates' (line : 4 column : 12)
ERROR:missing '.' at 'order' (line : 4 column : 25)
ERROR:no viable alternative at input 'history' (line : 4 column : 31)
ERROR:missing '.' at 'Then' (line : 5 column : 1)
ERROR:no viable alternative at input 'UserA' (line : 5 column : 6)
ERROR:missing '.' at 'should' (line : 5 column : 12)
ERROR:no viable alternative at input 'see' (line : 5 column : 19)
ERROR:missing '.' at 'one' (line : 5 column : 23)
ERROR:no viable alternative at input 'order' (line : 5 column : 27)
ERROR:missing '.' at 'a' (line : 5 column : 38)
ERROR:no viable alternative at input 'of' (line : 5 column : 46)
ERROR:no viable alternative at input '.' (line : 5 column : 52)
ERROR:extraneous input '99' expecting EOF (line : 5 column : 53)
ERROR:Couldn't resolve reference to Actor 'Given'. (line : 3 column : 1)
ERROR:Couldn't resolve reference to Actor 'authenticated'. (line : 3 column : 34)
ERROR:Couldn't resolve reference to Actor 'order'. (line : 4 column : 25)
ERROR:Couldn't resolve reference to Actor 'Then'. (line : 5 column : 1)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 5 column : 12)
ERROR:Couldn't resolve reference to Actor 'one'. (line : 5 column : 23)
ERROR:Couldn't resolve reference to Actor 'total'. (line : 5 column : 40)

```
### DSL-Rimay Score
DSL_Score: 58

Progressbar: ![58%](https://progress-bar.dev/58)

            


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
Final_score = 66.5

Progressbar: ![66.5%](https://progress-bar.dev/66.5)

