

# LLM Experiment Information
* Prefix:   Role-play
* Datetime: 04_11_2024__21:28:49
* UniqueID: 33c8bb2f-4c38-4bd5-a013-3218997d6530
* Gherkinscenario name: Gherkinscenario 12: Changing the currency of my cart
* LLM-temperature: 0.2

        

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
When UserA has "The Pug Mug" in the cart,
When UserA changes to "EUR" currency,
then system must display the grand total value as "€6.82".
``` 
            

### Researcher score
Researcher_score = -5




## DSL-Rimay Verification
```
ERROR:no viable alternative at input 'has' (line : 3 column : 12)
ERROR:missing ',' at 'the' (line : 3 column : 33)
ERROR:no viable alternative at input ',' (line : 3 column : 41)
ERROR:no viable alternative at input 'When' (line : 4 column : 1)
ERROR:no viable alternative at input 'to' (line : 4 column : 20)
ERROR:no viable alternative at input 'currency' (line : 4 column : 29)
ERROR:missing '.' at 'total' (line : 5 column : 36)
ERROR:no viable alternative at input 'value' (line : 5 column : 42)
ERROR:no viable alternative at input '.' (line : 5 column : 58)
ERROR:Couldn't resolve reference to Actor 'cart'. (line : 3 column : 37)
ERROR:Couldn't resolve reference to Actor 'system'. (line : 5 column : 6)
ERROR:Couldn't resolve reference to EObject 'grand'. (line : 5 column : 30)
ERROR:Couldn't resolve reference to Actor 'total'. (line : 5 column : 36)

```
### DSL-Rimay Score
DSL_Score: 81

Progressbar: ![81%](https://progress-bar.dev/81)

            


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
Final_score = 85.5

Progressbar: ![85.5%](https://progress-bar.dev/85.5)

