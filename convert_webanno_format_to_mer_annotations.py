"""This scripts converts the annotations resulting from Webanno (that are in Webanno TSV 3 format) into a simpler
format, the one output by MER"""

import re
import os
import shutil

# Path to the folder where are the annotation results. This folder probably has the name "annotation"
path_annotation_results = 'crowd_annotations/annotation/'
output_path = 'annotation_results_simple_tsv/'
target_entity_type = 'HPO'


# Clean everything inside output folder
shutil.rmtree(output_path)
os.makedirs(output_path)

# Each folder corresponds to one documents, inside being the annotations of each user for that document
folders_names = os.listdir(path_annotation_results)
for folder_name in folders_names:

    # Create new directory in the output folder
    os.makedirs(output_path + folder_name)

    file_names = os.listdir(path_annotation_results + folder_name)
    for file_name in file_names:

        with open(path_annotation_results + folder_name + '/' + file_name) as f:
            webanno_annotations = f.readlines()
            # Remove new lines and split by tabs (remember that we are processing a TSV file)
            webanno_annotations = map(lambda annotation: annotation.strip().split('\t'), webanno_annotations)

        mer_annotations = []
        mer_multiwords_annotations = {}

        for annotation in webanno_annotations:

            # If the line is empty or is a non-annotation, go to the next step of the loop
            if annotation[0] == '' or annotation[0].startswith('#'):
                continue

            if len(annotation) == 2:
                print "The following line has 2 columns ({}/{})".format(folder_name, file_name)
                print annotation
                print "Ignoring and continuing"
                print
                continue

            # Sometimes there is no column for entity type
            if len(annotation) == 3:
                print "The following line has 3 columns ({}/{})".format(folder_name, file_name)
                print annotation
                print "Assuming that the column missing is that last and that it to a non-annotation"
                annotation.append('_')
                print

            indexes = annotation[1]
            index_begin, index_end = indexes.split('-')

            token = annotation[2]
            entity_type = annotation[3]

            # In the MER file, I only want the words corresponding to annotations
            if entity_type == '_':
                continue

            if target_entity_type in entity_type.upper():

                # If in this columns there is just the entity we're looking for, create line for the output TSV
                if target_entity_type == entity_type.upper():
                    mer_annotations.append('{}\t{}\t{}\n'.format(index_begin, index_end, token))
                # Else we have to do some more work. Each multiword annotation is identified by a number and spans
                # more than one line. I save all the information about a multiword annotation using a dictionary
                else:
                    entitities = entity_type.split('|')
                    for entity in entitities:
                        entity_index = re.findall('\[(.*)\]', entity)[0]

                        if entity_index in mer_multiwords_annotations.keys():
                            mer_multiwords_annotations[entity_index]['token'] += ' {}'.format(token)
                            mer_multiwords_annotations[entity_index]['index_end'] = index_end
                        else:
                            mer_multiwords_annotations[entity_index] = {}
                            mer_multiwords_annotations[entity_index]['token'] = token
                            mer_multiwords_annotations[entity_index]['index_begin'] = index_begin
                            mer_multiwords_annotations[entity_index]['index_end'] = index_end

            # Just for debugging purporses.
            else:
                print 'This has a different entity type than the target entity type:'
                print annotation

        for annotation in mer_multiwords_annotations.values():
            mer_annotations.append('{}\t{}\t{}\n'.format(annotation['index_begin'], annotation['index_end'], annotation['token']))

        with open(output_path + folder_name + '/' + file_name, 'w') as f:
            for annotation in mer_annotations:
                f.write(annotation)
