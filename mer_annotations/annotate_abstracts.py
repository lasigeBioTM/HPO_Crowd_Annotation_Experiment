import subprocess
import os
import copy

# After putting the HPO lexicon on the data/ folder and processing it using the "produce_data_files.sh" script


# Change accordingly
mer_path = '/home/lcampos/Development/MER/'
abstract_texts_path = '/home/lcampos/Development/HPO_Crowd_Annotation_Experiment/text/'
mer_annotations_path = '/home/lcampos/Development/HPO_Crowd_Annotation_Experiment/mer_annotations/annotations/'

bash_command_template = ['bash', 'get_entities.sh', '', 'hpo']

# Change to the MER directory
os.chdir(mer_path)

# Get list of all abstracts file names
abstract_file_names = os.listdir(abstract_texts_path)

# Annotate each abstract
for abstract_file_name in abstract_file_names:
    with open(abstract_texts_path + abstract_file_name) as abstract_file:
        abstract_text = abstract_file.read()

        abstract_text_before_processing = copy.copy(abstract_text)

        # Removes newlines from abstracts.  Workaround of a bug in MER.
        abstract_text = abstract_text.replace('\n', ' ')

        # Confirm that the length of the text was not altered during processing
        assert len(abstract_text_before_processing) == len(abstract_text)

        # Fills template
        bash_command_template[2] = abstract_text

        # Run MER from Python
        annotations = subprocess.check_output(bash_command_template)

        # Write annotations to a new file
        with open(mer_annotations_path + abstract_file_name + '.tsv', 'w') as f:
            f.write(annotations)
