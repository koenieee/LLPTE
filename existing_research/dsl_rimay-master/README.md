# Rimay a Controlled Natural Language for Functional Requirements

Rimay is a domain-specific language for writing functional requirements in the financial domain.   Rimay's editor is implemented  using the Xtext language engineering framework.

## Prerequisites:
- Java Runtime Environment
- Eclipse IDE for Java and DSL Developers

## Steps:
1. Open Eclipse and select a workspace
2. Use the Import wizard and select `General > Existing Projects into Workspace` to import the Rimay plugins (ide, ui, and dsl_rimay) contained under the `dsl-rimay` folder.
3. Run the file `dsl_rimay/org.xtext.dsl_rimay/src/org/xtext/Dsl_rimay.xtext` selecting the option `Generate Xtext Artifacts`.
4. Select the root project `dsl_rimay/org.xtext.dsl_rimay/` and click the `Run` button selectin `Run as Eclipse application`
5. A new instance of Eclipse including Rimay's editor will be opened
6. Create a file with the extension `.rimay` and you can start writing functional requirements



## Examples of Functional Requirements written in Rimay:

```

Actors: actor SystemA, actor SystemB, actor SystemC
Classes: class Instruction := description record
\\Requirement 1:
When SystemB receives an "email alert" from SystemA, SystemB must send an Instruction to SystemC.
\\Requirement 2:
If Instruction.description contains a "Keyword" or Instruction.record is "Live", then SystemA must create "A".
\\Requirement 3:
If the following conditions are satisfied:
- the "Instruction" has the properties described on "Section Y",
- the "Instruction" has the properties: "Owner, Status and Settlement Date" and
- the "Account Number" field contains "0000", then SystemA must send Instruction to SystemB.
\\Requirement 4:
The User must upload the "excel file" to the "SystemA".
\\Requirement 5:
The SystemA must do the following actions in sequence:
 1 create an "Instruction"
 2 send "Instruction" to SystemB.

```


## License:
Rimay is © 2023 University of Luxembourg and licensed under the MIT license.
Please read NOTICE.txt for details.
