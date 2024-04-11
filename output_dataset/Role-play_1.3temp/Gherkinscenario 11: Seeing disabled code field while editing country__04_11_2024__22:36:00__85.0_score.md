

# LLM Experiment Information
* Prefix:   Role-play
* Datetime: 04_11_2024__22:36:00
* UniqueID: d314d67e-363a-4124-b07d-ef61c1116c5b
* Gherkinscenario name: Gherkinscenario 11: Seeing disabled code field while editing country
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: SystemA has country "United States"
When: UserA wants to edit this country
Then: the code field should be disabled
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
Given: SystemA has country "United States"
When: UserA wants to edit this country
Then: the code field should be disabled
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
When: SystemA has "country value" called  "United States"
When UserA seeks to change "country"
then ("the code field") must be "not able to edit".
``` 
            

### Researcher score
Researcher_score = -5




## DSL-Rimay Verification
```
ERROR:no viable alternative at input ':' (line : 3 column : 5)
ERROR:missing ',' at 'SystemA' (line : 3 column : 7)
ERROR:no viable alternative at input 'has' (line : 3 column : 15)
ERROR:no viable alternative at input 'called' (line : 3 column : 35)
ERROR:no viable alternative at input '"United States"' (line : 3 column : 43)
ERROR:no viable alternative at input 'When' (line : 4 column : 1)
ERROR:no viable alternative at input 'to' (line : 4 column : 18)
ERROR:missing ',' at 'be' (line : 5 column : 30)
ERROR:no viable alternative at input '"not able to edit"' (line : 5 column : 33)
ERROR:no viable alternative at input '.' (line : 5 column : 51)
ERROR:Couldn't resolve reference to Actor 'called'. (line : 3 column : 35)
ERROR:Couldn't resolve reference to Actor 'seeks'. (line : 4 column : 12)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 4 column : 6)
ERROR:Couldn't resolve reference to Actor 'be'. (line : 5 column : 30)

```
### DSL-Rimay Score
DSL_Score: 80

Progressbar: ![80%](https://progress-bar.dev/80)

            


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
Final_score = 85.0

Progressbar: ![85.0%](https://progress-bar.dev/85.0)

