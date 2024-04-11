

# LLM Experiment Information
* Prefix:   Role-play
* Datetime: 04_11_2024__20:36:46
* UniqueID: 4fefca13-6e8f-4a5c-a2ab-92829de3916a
* Gherkinscenario name: Gherkinscenario 4: User presses button.
* LLM-temperature: 0.2

        

## Gherkin Input
```
Given: UserA navigates to the login page
When: UserA clicks on button
Then: SystemA refreshes page
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
Given: UserA navigates to the login page
When: UserA clicks on button
Then: SystemA refreshes page
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
When UserA navigates to "login page",
When UserA clicks on "button",
then SystemA refreshes "page".
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'to' (line : 3 column : 22)
ERROR:missing RULE_ID at ',' (line : 4 column : 30)
ERROR:no viable alternative at input 'refreshes' (line : 5 column : 14)
ERROR:Couldn't resolve reference to Actor 'navigates'. (line : 3 column : 12)
ERROR:Couldn't resolve reference to Quantifier 'UserA'. (line : 3 column : 6)

```
### DSL-Rimay Score
DSL_Score: 89

Progressbar: ![89%](https://progress-bar.dev/89)

            


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
Final_score = 97.0

Progressbar: ![97.0%](https://progress-bar.dev/97.0)

