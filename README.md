# Brief Explanation of the Organization of the repository

The scripts usually have some parameters that can be changed, mostly to indicate paths to folders.

### data/
Contains abstract texts and corresponding gold-annotations. [Source](https://academic.oup.com/database/article-lookup/doi/10.1093/database/bav005). 

### lexicon_creation/
Here you will find a script that extracts all the entity names from the HPO .obo file into a .txt lexicon file to be used by MER.

### mer_annotations/
Contains script that annotates, using MER, all the abstracts of the corpus. It also contains the folder **annotations/** that contains these MER annotations.

### mer_annotations_webanno/
Contains script to convert annotations in the MER format to Webanno TSV 3 format, so that they can be imported to Webanno web application.

### compare_annotations_with_gold_standard.ipynb
Code to compare annotations of the MER format with the gold-standard annotations.

### convert_webanno_format_to_mer_annotations.py
Converts annotations exported from Webanno (in TSV3 format) to the easier-to-work-with MER format. The output is folder with the same strucure as the **annotation** folder exported from Webanno.

### create_aggregate_annotations.py
Aggregate crowd annotations into just one annotation file by document. 

