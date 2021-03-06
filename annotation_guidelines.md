1. Phenotype concepts should only be considered if they are present in a canonical form—e.g. include ‘hypoplastic nails’ or ‘nail hypoplasia’, but not ‘nails were hypoplastic’.

2. Conjunctive terms are allowed—e.g. ‘synostosis of some carpal and tarsal bones’.

3. Subject to the type of conjunction, atomic text spans are to be annotated with the corresponding HPO concepts. For example, the text span ‘synostosis of some carpal and tarsal bones’ represents a conjunction of two phenotype concepts: HP: 0008368 (Synostosis involving tarsal bones) and HP: 0009702 (Synostosis involving the carpal bones). Since the qualifier is preceding the anatomical conjunction, the entire text span should be annotated with both HPO concepts. On the other hand, when the qualifier is succeeding the anatomical conjunction—i.e. a mirror of the previous case—the text span should be split into the corresponding atomic phenotypes. For example, ‘branchial arch, otic and renal malformations’ results in three annotations:

* ‘branchial arch, otic and renal malformations’—HP: 0009794 (Branchial anomaly)
* ‘otic and renal malformations’—HP: 0000598 (Abnormality of the ear)
* ‘renal malformations’—HP: 0000792 (Abnormal renal morphology)

4. Negated phenotypes should be included—i.e. the text span ‘kidney anomalies’ in the context of ‘no kidney anomalies were found’ should be annotated with HP: 0000077 (Abnormality of the kidney). Here, the assumption was that negation can be dealt with at a different level and via other means.

**In:** Groza T, Köhler S, Doelken S, et al. Automatic concept recognition using the Human Phenotype Ontology reference and test suite corpora. Database: The Journal of Biological Databases and Curation. 2015;2015:bav005. doi:10.1093/database/bav005.
