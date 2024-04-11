

# LLM Experiment Information
* Prefix:   Role-play
* Datetime: 04_11_2024__22:37:52
* UniqueID: fe97946e-90d9-44f0-b101-0ebeadd98aa9
* Gherkinscenario name: Gherkinscenario 12: Changing the currency of my cart
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: UserA has product "The Pug Mug" in the cart
When: UserA switches to the "EUR" currency
Then: the grand total value should be "€6.82"
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
Given: UserA has product "The Pug Mug" in the cart
When: UserA switches to the "EUR" currency
Then: the grand total value should be "€6.82"
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
When "UserA" has "product" in the cart, 
When "UserA" switches to "EUR" currency, 
then the grand total value should be "€6.82"
``` 
            

### Researcher score
Researcher_score = 15




## DSL-Rimay Verification
```
ERROR:mismatched input 'has' expecting ',' (line : 3 column : 14)
ERROR:missing '.' at 'the' (line : 3 column : 31)
ERROR:no viable alternative at input ',' (line : 3 column : 39)
ERROR:no viable alternative at input 'When' (line : 4 column : 1)
ERROR:missing ',' at 'switches' (line : 4 column : 14)
ERROR:no viable alternative at input 'to' (line : 4 column : 23)
ERROR:no viable alternative at input 'currency' (line : 4 column : 32)
ERROR:no viable alternative at input ',' (line : 4 column : 40)
ERROR:no viable alternative at input 'the' (line : 5 column : 6)
ERROR:no viable alternative at input 'total' (line : 5 column : 16)
ERROR:missing '.' at 'should' (line : 5 column : 28)
ERROR:no viable alternative at input 'be' (line : 5 column : 35)
ERROR:mismatched input '<EOF>' expecting '.' (line : 5 column : 38)
ERROR:Couldn't resolve reference to Actor 'cart'. (line : 3 column : 35)
ERROR:Couldn't resolve reference to Actor 'switches'. (line : 4 column : 14)
ERROR:Couldn't resolve reference to Actor 'currency'. (line : 4 column : 32)
ERROR:Couldn't resolve reference to Actor 'grand'. (line : 5 column : 10)
ERROR:Couldn't resolve reference to Actor 'should'. (line : 5 column : 28)

```
### DSL-Rimay Score
DSL_Score: 66

Progressbar: ![66%](https://progress-bar.dev/66)

            


## Rimay Paska Verification
```
File generated_rimay.csv.csv
Smells found in this document: 
Non-atomic requirement: 0
Incomplete requirement: 0
Incorrect order requirement: 0
Coordination ambiguity: 0
Not requirement: ,0
Incomplete condition: 1
Incomplete system response: 0
Passive voice: 0
Not precise verb: 0
Number Req with smells: 1

```
### Paska Score
PASKA_Score: 90

Progressbar: ![90%](https://progress-bar.dev/90)

            

### Final Score
Final_score = 93.0

Progressbar: ![93.0%](https://progress-bar.dev/93.0)

