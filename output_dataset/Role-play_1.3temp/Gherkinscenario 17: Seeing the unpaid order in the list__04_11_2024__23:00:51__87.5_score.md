

# LLM Experiment Information
* Prefix:   Role-play
* Datetime: 04_11_2024__23:00:51
* UniqueID: 00071baa-fa36-4659-972d-2d735955fa09
* Gherkinscenario name: Gherkinscenario 17: Seeing the unpaid order in the list
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: UserA logged in as "john@example.com"
When: UserA views order history
Then: UserA should sees one order with total of $29.99
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
When UserA accesses "order history",
then system should display "one order" with total of "$29.99".
``` 
            

### Researcher score
Researcher_score = -5




## DSL-Rimay Verification
```
ERROR:no viable alternative at input ',' (line : 3 column : 36)
ERROR:no viable alternative at input 'should' (line : 4 column : 13)
ERROR:missing '.' at 'total' (line : 4 column : 45)
ERROR:no viable alternative at input 'of' (line : 4 column : 51)
ERROR:no viable alternative at input '.' (line : 4 column : 62)
ERROR:Couldn't resolve reference to Actor 'accesses'. (line : 3 column : 12)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 6)
ERROR:Couldn't resolve reference to Actor 'system'. (line : 4 column : 6)
ERROR:Couldn't resolve reference to Actor 'total'. (line : 4 column : 45)

```
### DSL-Rimay Score
DSL_Score: 85

Progressbar: ![85%](https://progress-bar.dev/85)

            


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
Final_score = 87.5

Progressbar: ![87.5%](https://progress-bar.dev/87.5)

