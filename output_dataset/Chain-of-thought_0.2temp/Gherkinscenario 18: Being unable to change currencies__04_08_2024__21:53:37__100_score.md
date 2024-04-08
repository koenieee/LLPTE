

# LLM Experiment Information
* Prefix:   Chain-of-thought
* Datetime: 04_08_2024__21:53:37
* UniqueID: a5c27bb1-f4fe-4e4b-ae53-50bb985f1e77
* Gherkinscenario name: Gherkinscenario 18: Being unable to change currencies
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
While the Order does not exist, 
When the Order_Issuer (OI ) executes Create a Subscription_Order, 
then the Order is created and its settlement_method is set to FOP.


Gherkin input 2:
Given: a verification email has already been sent to "operator"
When: operator verifies his account using the link from this email
Then: operator should be notified that the verification was successful

Rimay output 2:
While the "verification email" contains a "verification link" 
When operator validates "email address" following the "verification link", 
then system must notify "with verification successful" to operator.  
 

Gherkin input 3: 
Given: visitor is edits the address of "Fletcher Ren"
When: visitor deletes the street
Then: visitor should still be on the "Fletcher Ren" address edit page


Rimay output 3:
While visitor is "edits the adress of Fletcher Ren" 
When visitor removes "the street", 
then website must show "the edit address page".


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
While the exchange rate of "US Dollar" to "British Pound" is 1.30,
When UserA intends to modify this exchange rate,
then UserA must observe that the source currency is deactivated.
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'rate' (line : 3 column : 20)
ERROR:no viable alternative at input 'of' (line : 3 column : 25)
ERROR:no viable alternative at input '.' (line : 3 column : 63)
ERROR:missing EOF at '30' (line : 3 column : 64)
ERROR:Couldn't resolve reference to ActorOrClassOrProperty 'exchange'. (line : 3 column : 11)
ERROR:Couldn't resolve reference to Actor 'rate'. (line : 3 column : 20)

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
Final_score = 100

Progressbar: ![100%](https://progress-bar.dev/100)

