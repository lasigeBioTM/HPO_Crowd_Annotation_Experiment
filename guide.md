# 1st Day - HPO Lexicon construction and MER annotations

### Goals
- [ ] Create lexicon with terms from HPO (Human Phenotype Ontology)
- [ ] Annotate abstracts using MER

### Step-by-step guide

#### 1. Turn on computers and enter Linux Operating System

#### 2. Clone repository to your machine 

```
cd {{ folder_in_which_you_want_to_work }} # ex: ~/Desktop
git clone https://github.com/lasigeBioTM/HPO_Crowd_Annotation_Experiment
```

Or download it directly from the repository. 

#### 3. Download HPO .obo file and analyse it 

Download it from here:
http://human-phenotype-ontology.github.io/

OBO is a file format that can be used to represent ontologies. Open the file in some text editor and analyse it. Our goal is to extract from this file all the names that represent some entity. Think how would you do it. 

#### 4. Create lexicon using Python

Using Python programming language, extract from the .obo file all the names that represent some entity and put it in some .txt file. This will be our lexicon. It will contain all the terms in HPO. 


# 2nd Day - Crowd Annotation 

### Goals
- [ ] Crowd annotation activities 
- [ ] Compare crowd annotations with gold annotations 
- [ ] Results discussion
