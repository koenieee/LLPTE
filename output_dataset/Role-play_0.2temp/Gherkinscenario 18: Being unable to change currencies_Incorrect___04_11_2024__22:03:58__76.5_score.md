

# LLM Experiment Information
* Prefix:   Role-play
* Datetime: 04_11_2024__22:03:58
* UniqueID: 56745d58-eaee-41e1-a58b-417697c4f03c
* Gherkinscenario name: Gherkinscenario 18: Being unable to change currencies_Incorrect_
* LLM-temperature: 0.2

        

## Gherkin Input
```
Given: the exchange rate of "US Dollar" to "British Pound" is 1.30
When: UserA wants to edit this exchange rate
Then: UserA should see that the source currency is disabled
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
 the "verification email" contains a "verification link" 
```

2. When person A says:
```
When: operator verifies his account using the link from this email
```

2. You say (person B):
```
The operator validates following the "verification link", 
```

3. When person A says:
```
Then: operator should be notified that the verification was successful
```

3. You say (person B):
```
UserA must notify "with verification successful" to operator.  
```


So person B pays special attention to the common structure of Rimay. 
Output the total rimay output as follows:

1.
2.
3.

Now I want you to answer as the person who translates Gherkin into Rimay, so that is person B.
Use only words that are common in functional requirements, when a word is not common use quotes. 
Do not output empty rimay structures!
        

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
1. The "exchange rate" between "US Dollar" and "British Pound" must be set to 1.30
2. UserA is able to modify the "exchange rate"
3. UserA must observe that the source currency is inactive
``` 
            

### Researcher score
Researcher_score = -10




## DSL-Rimay Verification
```
ERROR:missing EOF at '1' (line : 3 column : 1)

```
### DSL-Rimay Score
DSL_Score: 83

Progressbar: ![83%](https://progress-bar.dev/83)

            


## Rimay Paska Verification
```
File generated_rimay.csv.csv
Smells found in this document: 
Non-atomic requirement: 1
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
PASKA_Score: 90

Progressbar: ![90%](https://progress-bar.dev/90)

            

### Final Score
Final_score = 76.5

Progressbar: ![76.5%](https://progress-bar.dev/76.5)

