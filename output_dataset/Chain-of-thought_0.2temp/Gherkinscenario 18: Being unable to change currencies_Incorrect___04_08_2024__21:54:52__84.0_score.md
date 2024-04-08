

# LLM Experiment Information
* Prefix:   Chain-of-thought
* Datetime: 04_08_2024__21:54:52
* UniqueID: 89b3d005-3c0b-4c9a-8238-ba4b18e441c5
* Gherkinscenario name: Gherkinscenario 18: Being unable to change currencies_Incorrect_
* LLM-temperature: 0.2

        

## Gherkin Input
```
Given: the exchange rate of "US Dollar" to "British Pound" is 1.30
When: UserA wants to edit this exchange rate
Then: UserA should see that the source currency is disabled
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
When UserA modifies the exchange rate between "US Dollar" and "British Pound", 
then UserA must observe that the source currency is not editable.
``` 
            

### Researcher score
Researcher_score = -5




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'the' (line : 3 column : 21)
ERROR:no viable alternative at input 'rate' (line : 3 column : 34)
ERROR:missing '.' at 'between' (line : 3 column : 39)
ERROR:no viable alternative at input '"US Dollar"' (line : 3 column : 47)
ERROR:no viable alternative at input 'UserA' (line : 4 column : 6)
ERROR:no viable alternative at input 'observe' (line : 4 column : 17)
ERROR:no viable alternative at input 'that' (line : 4 column : 25)
ERROR:no viable alternative at input 'the' (line : 4 column : 30)
ERROR:no viable alternative at input 'currency' (line : 4 column : 41)
ERROR:extraneous input 'editable' expecting '.' (line : 4 column : 57)
ERROR:Couldn't resolve reference to Actor 'modifies'. (line : 3 column : 12)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 6)
ERROR:Couldn't resolve reference to Actor 'exchange'. (line : 3 column : 25)
ERROR:Couldn't resolve reference to Actor 'between'. (line : 3 column : 39)
ERROR:Couldn't resolve reference to Actor 'observe'. (line : 4 column : 17)
ERROR:Couldn't resolve reference to Actor 'source'. (line : 4 column : 34)

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
Final_score = 84.0

Progressbar: ![84.0%](https://progress-bar.dev/84.0)

