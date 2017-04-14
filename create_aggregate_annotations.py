import os
import shutil

# Path to the folder where the crowd annotations (simple TSV versions) are.
path_to_crowd_annotations = 'annotation_results_simple_tsv/'

# Vote threshold for a annotation be in the aggregated annotation. 0.5 means that 50% of the crowd have to annotate
# a term to it to be included in the aggregated annotations
threshold = 0.5

aggregated_results_directory_name = 'aggregated_results_{}/'.format(threshold)
if not os.path.exists(aggregated_results_directory_name):
    os.makedirs(aggregated_results_directory_name)
else:
    # Clean everything inside output folder
    shutil.rmtree(aggregated_results_directory_name)
    os.makedirs(aggregated_results_directory_name)


document_names = os.listdir(path_to_crowd_annotations)
for document_name in document_names:

    annotations_ballot = {}

    crowd_annotations_file_names = os.listdir(path_to_crowd_annotations + document_name)
    vote_threshold = len(crowd_annotations_file_names) * threshold

    for file_name in crowd_annotations_file_names:

        with open(path_to_crowd_annotations + document_name + '/' + file_name) as f:
            annotations = f.readlines()

            for annotation in annotations:
                if annotation in annotations_ballot.keys():
                    annotations_ballot[annotation] += 1
                else:
                    annotations_ballot[annotation] = 1

    with open(aggregated_results_directory_name + document_name, 'w') as f:
        for annotation, number_votes in annotations_ballot.iteritems():
            if number_votes > vote_threshold:
                f.write(annotation)
