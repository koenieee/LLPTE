

# LLM Experiment Information
* Prefix:   Role-play
* Datetime: 04_11_2024__17:09:48
* UniqueID: 2603b9f9-0ae0-4e8c-a23f-908e2c3d0b8a
* Gherkinscenario name: Gherkinscenario 2: Money withdraw from bank account_Incorrect_
* LLM-temperature: 1.3

        

## Gherkin Input
```
Given: UserA bank account is in credit
When: UserA attempts to withdraw an amount less than UserA card's limit
Then: the withdrawal should be complete without errors or warnings
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
Given: UserA bank account is in credit
When: UserA attempts to withdraw an amount less than UserA card's limit
Then: the withdrawal should be complete without errors or warnings
```

### Question:
Can you translate the input above into the specified language Rimay CNL?

### Output indicator
Output only the translated Rimay CNL text and nothing else!


## Rimay Output
```
When operator "bank account" is in credit, 
When operator tries to withdraw an "amount" less than card's "limit",
then system must complete the "withdrawal" without "errors" or "warnings".
``` 
            
