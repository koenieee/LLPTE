

# LLM Experiment Information
* Prefix:   Role-play
* Datetime: 04_11_2024__20:21:46
* UniqueID: 0f2bce8e-fe55-4b2e-83d4-fc05b6554f84
* Gherkinscenario name: Gherkinscenario 1: Requesting the cash from a creditworthy account
* LLM-temperature: 0.2

        

## Gherkin Input
```
Given: that the account is creditworthy
When: UserA requests the cash
Then: ensure the account is debited
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
Given: that the account is creditworthy
When: UserA requests the cash
Then: ensure the account is debited
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
When "account" is "creditworthy",
When "UserA" requests "cash",
then ensure "account" is "debited".
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:mismatched input 'is' expecting ',' (line : 3 column : 16)
ERROR:missing '.' at 'When' (line : 4 column : 1)
ERROR:mismatched input 'requests' expecting ',' (line : 4 column : 14)
ERROR:missing '.' at 'ensure' (line : 5 column : 6)
ERROR:no viable alternative at input '"account"' (line : 5 column : 13)
ERROR:no viable alternative at input '.' (line : 5 column : 35)
ERROR:Couldn't resolve reference to Actor 'ensure'. (line : 5 column : 6)

```
### DSL-Rimay Score
DSL_Score: 87

Progressbar: ![87%](https://progress-bar.dev/87)

            


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
Final_score = 96.0

Progressbar: ![96.0%](https://progress-bar.dev/96.0)

