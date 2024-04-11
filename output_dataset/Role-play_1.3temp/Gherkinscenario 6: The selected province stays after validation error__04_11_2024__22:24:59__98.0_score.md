

# LLM Experiment Information
* Prefix:   Role-play
* Datetime: 04_11_2024__22:24:59
* UniqueID: 581d5ba3-2b67-47ca-98af-03b3cb8c4eb9
* Gherkinscenario name: Gherkinscenario 6: The selected province stays after validation error
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: UserA is editing the address of "Fletcher Ren"
When: UserA removes the street
Then: UserA should still be on the "Fletcher Ren" address edit page
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
When UserA modifies the address of "Fletcher Ren",  
When UserA deletes the street,  
Then the system must keep UserA on the "Fletcher Ren" address modification page.
``` 
            

### Researcher score
Researcher_score = 10




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'the' (line : 3 column : 21)
ERROR:no viable alternative at input 'of' (line : 3 column : 33)
ERROR:no viable alternative at input 'When' (line : 4 column : 1)
ERROR:no viable alternative at input 'the' (line : 5 column : 6)
ERROR:missing '.' at 'system' (line : 5 column : 10)
ERROR:no viable alternative at input 'keep' (line : 5 column : 22)
ERROR:no viable alternative at input 'UserA' (line : 5 column : 27)
ERROR:missing '.' at 'the' (line : 5 column : 36)
ERROR:extraneous input '"Fletcher Ren"' expecting RULE_ID (line : 5 column : 40)
ERROR:no viable alternative at input 'modification' (line : 5 column : 63)
ERROR:Couldn't resolve reference to Actor 'modifies'. (line : 3 column : 12)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 6)
ERROR:Couldn't resolve reference to Actor 'address'. (line : 3 column : 25)
ERROR:Couldn't resolve reference to PropertyOrLabel 'street'. (line : 4 column : 24)
ERROR:Couldn't resolve reference to Actor 'Then'. (line : 5 column : 1)
ERROR:Couldn't resolve reference to Actor 'system'. (line : 5 column : 10)
ERROR:Couldn't resolve reference to Actor 'keep'. (line : 5 column : 22)
ERROR:Couldn't resolve reference to Actor 'address'. (line : 5 column : 55)

```
### DSL-Rimay Score
DSL_Score: 76

Progressbar: ![76%](https://progress-bar.dev/76)

            


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
Final_score = 98.0

Progressbar: ![98.0%](https://progress-bar.dev/98.0)

