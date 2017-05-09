# Main Question: How do crowd annotations compare with expert annotations? 

## 1st Day - HPO Lexicon construction and MER annotations

### Goals
- [ ] Create lexicon with terms from HPO (Human Phenotype Ontology)
- [ ] Annotate abstracts using MER (Minimal Named-Entity Recognizer)

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

#### 5. Install [MER (Minimal Named-Entity Recognizer)](https://github.com/lasigeBioTM/MER)

Don't forget to run the test script to check if everything is ok. 

#### 6. Play with MER

#### 7. Create script to create annotations for all abstracts 

Create Python script to annotate all the abstracts found in the [/data folder of this repo](https://github.com/lasigeBioTM/HPO_Crowd_Annotation_Experiment/tree/master/data).

## 2nd Day - Crowd Annotation 

### Goals
- [ ] Crowd annotation activity
- [ ] Compare crowd annotations with gold annotations 
- [ ] Results discussion

#### 1. Go to [LaSIGE Webanno page](http://www.lasige.di.fc.ul.pt/webtools/webanno3/welcome.html)

- On the main page click in "Correction"
- Choose the "BioSys Crowd Annotations Sandbox" project to experiment with the app

[
DEMO BY INSTRUCTOR
* How to accept suggestion
* How to add new annotation 
* How to delete annotation
* Walk through annotation of document 998578
]

#### 2. Read the [guidelines](https://github.com/lasigeBioTM/HPO_Crowd_Annotation_Experiment/blob/master/annotation_guidelines.md)

#### 3. Annotate!

- Change to the "BioSys Crowd Annotations" project
- Use [this](http://compbio.charite.de/hpoweb/showterm) or [this](https://bioportal.bioontology.org/ontologies/HP/?p=classes&conceptid=root) app to help you
- Annotate all 6 documents
- To facilitate, start with the first document and press "Next" in the "Document" tab when you're finished with a document

#### 4. Discuss results

- Compare crowd annotations with gold annotations
- Change annotation acceptance threshold and see how does that affect the result
- Are crowd annotations better than just using MER?
- Should we use crowd annotations instead of gold annotations?



