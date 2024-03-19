# LLPTE
LLPTE (LLM Prompt Technique Experiments). Repository to experiment with different prompting techniques for translating Gherkin Acceptance Criteria into Rimay (CNL) System Requirements 



# Setup

Use conda and enable extra channels (such as conda-forge)


Deactive conda:
```
conda deactivate
conda env remove -n smell-detector
```

Active conda:
```
conda env create -f conda_llpte.yml
conda activate smell-detector
```

#


# Run this application with python:

- Ubuntu version used: 22.04, full desktop edition. (server is also fine)
- Install requirements:
```bash
pip install -r requirements.txt
python3 main.py
```

Make sure to open port 8080 on webserver to access nicegui
For standalone modes add the parameter: standalone

Results will be logged in prompt_logging folder, sorted by LLM-prompting techniqnue.
Filename contains score from DSL Rimay and Paska.

```bash

python3 main.py standalone 0 20

```

Means run script standalone and use acceptance criteria 0 - 20.

Input dataset for Gherkin is inspired by https://zenodo.org/records/6460854
See input_dataset.xml

# Notes to run paska tooling
use full Java 8 JDK with JFX runtime. Do not use the small version of java on Linux Ubuntu.
I also changed the conda environment file to be compatible with Ubuntu instead of OSX.

To install correct version of JDK: 
https://bell-sw.com/pages/repositories/#apt

```bash
wget -q -O - https://download.bell-sw.com/pki/GPG-KEY-bellsoft | sudo apt-key add -
echo "deb [arch=amd64] https://apt.bell-sw.com/ stable main" | sudo tee /etc/apt/sources.list.d/bellsoft.list
sudo apt-get update
sudo apt-get install bellsoft-java8-runtime-full
```

Also download the following distsim tagger file: 
```
https://github.com/amiangshu/SentiSE/blob/master/edu/stanford/nlp/models/pos-tagger/english-left3words/english-left3words-distsim.tagger
```
And see the following file for needed modifications to paths: `/LLPTE/rimay_verification.py`
Also, there is no error when the directory of preproccesing tooling is not found, be aware. And use full paths for everything.

I precompiled the jar files for Paska and DSL Rimay.