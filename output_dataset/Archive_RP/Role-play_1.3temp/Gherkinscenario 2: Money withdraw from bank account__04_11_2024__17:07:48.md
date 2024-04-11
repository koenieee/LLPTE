

# LLM Experiment Information
* Prefix:   Role-play
* Datetime: 04_11_2024__17:07:48
* UniqueID: d83d5e95-563f-4b1c-aadb-e78c75031cb1
* Gherkinscenario name: Gherkinscenario 2: Money withdraw from bank account
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

You are person B.

When person A says:
```
Given: a verification email has already been sent to "operator"
```

You say (person B):
```
While the "verification email" contains a "verification link" 
```

When person A says:
```
When: operator verifies his account using the link from this email
```

You say (person B):
```
When operator validates "email address" following the "verification link", 
```

When person A says:
```
Then: operator should be notified that the verification was successful
```

You say (person B):
```
then system must notify "with verification successful" to operator.  
```


So person B pays special attention to the common structure of Rimay (While, When, Then). 
Output the total rimay output as follows:

While
When
then

Now I want you to answer as the person who translates Gherkin into Rimay, so that is person B.
Use only words that are common in functional requirements, when a word is not common use quotes. 
Do not output empty rimay structure!
        

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
When
When UserA requests to withdraw an amount less than "card limit",
then system should complete the withdrawal operation without any errors or warnings.
``` 
            
