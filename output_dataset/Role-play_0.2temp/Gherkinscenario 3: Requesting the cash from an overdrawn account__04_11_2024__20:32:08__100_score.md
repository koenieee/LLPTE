

# LLM Experiment Information
* Prefix:   Role-play
* Datetime: 04_11_2024__20:32:08
* UniqueID: 0d2ae570-85a2-4450-b2f1-54aede8200e6
* Gherkinscenario name: Gherkinscenario 3: Requesting the cash from an overdrawn account
* LLM-temperature: 0.2

        

## Gherkin Input
```
Given: that the account is overdrawn
When: UserA requests the cash
Then: ensure the rejection message is displayed
```
    



## Input prompt, technique: Role-Play


Behave like a person who writes the Controlled Natural Language (CNL) Rimay.
Rimay is a language that is defined in different components. 
You are a person that translates Gherkin acceptance criteria into Rimay system requirements.
A person that translates Gherkin in Rimay behaves like the following:

One person (person A) speaks Gherkin, the acceptance criteria language.
The other person (person B) speaks Rimay, a functional requirement Controlled Natural Language (CNL).

The conversation goes as follows

1. When person A says:
```
Given: a verification email has already been sent to "operator"
```

1. You say (person B):
```
While the "verification email" contains a "verification link" 
```

2. When person A says:
```
When: operator verifies his account using the link from this email
```

2. You say (person B):
```
When operator validates "email address" following the "verification link", 
```

3. When person A says:
```
Then: operator should be notified that the verification was successful
```

3. You say (person B):
```
then system must notify "with verification successful" to operator.  
```


So person B pays special attention to the common structure of Rimay (While, When, Then). 
Output the total rimay output as follows:

While 1.
When 2.
then 3.

Now I want you to answer as the person who translates Gherkin into Rimay, so that is person B.
Use only words that are common in functional requirements, when a word is not common use quotes. 
Do not output empty rimay structures!
        

### Input Data
Use the following Gherkin acceptance criteria input: 
```
Given: that the account is overdrawn
When: UserA requests the cash
Then: ensure the rejection message is displayed
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
When account is "overdrawn",
When UserA requests "cash",
then system must display "rejection message".
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'is' (line : 3 column : 14)
ERROR:mismatched input '"cash"' expecting RULE_ID (line : 4 column : 21)
ERROR:Couldn't resolve reference to Actor 'account'. (line : 3 column : 6)
ERROR:Couldn't resolve reference to Actor 'system'. (line : 5 column : 6)

```
### DSL-Rimay Score
DSL_Score: 95

Progressbar: ![95%](https://progress-bar.dev/95)

            


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

