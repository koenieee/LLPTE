

# LLM Experiment Information
* Prefix:   Chain-of-thought
* Datetime: 04_08_2024__22:12:09
* UniqueID: 59464075-7bb0-40cf-bdd8-2e438c0b946a
* Gherkinscenario name: Gherkinscenario 6: The selected province stays after validation error_Incorrect_
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: UserA is editing the address of "Fletcher Ren"
When: UserA removes the street
Then: UserA should still be on the "Fletcher Ren" address edit page
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
Given: UserA is editing the address of "Fletcher Ren"
When: UserA removes the street
Then: UserA should still be on the "Fletcher Ren" address edit page
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
While UserA is editing the address of "Ren" 
then keep UserA on the "Ren" address edit page.
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'the' (line : 3 column : 24)
ERROR:no viable alternative at input 'of' (line : 3 column : 36)
ERROR:no viable alternative at input 'keep' (line : 4 column : 6)
ERROR:no viable alternative at input 'UserA' (line : 4 column : 11)
ERROR:missing '.' at 'the' (line : 4 column : 20)
ERROR:extraneous input '"Ren"' expecting RULE_ID (line : 4 column : 24)
ERROR:no viable alternative at input 'edit' (line : 4 column : 38)
ERROR:Couldn't resolve reference to Quantifier 'editing'. (line : 3 column : 16)
ERROR:Couldn't resolve reference to Actor 'address'. (line : 3 column : 28)
ERROR:Couldn't resolve reference to Actor 'keep'. (line : 4 column : 6)
ERROR:Couldn't resolve reference to Actor 'address'. (line : 4 column : 30)

```
### DSL-Rimay Score
DSL_Score: 83

Progressbar: ![83%](https://progress-bar.dev/83)

            


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
Final_score = 69.0

Progressbar: ![69.0%](https://progress-bar.dev/69.0)

