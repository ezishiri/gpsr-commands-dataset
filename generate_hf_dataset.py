import csv

def txts_to_csv(txt_file_paths, csv_file_path):
    row_id = 0  # Initialize row ID counter

    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['id', 'utterance', 'logical_form'])  # Write the header row

        for txt_file_path in txt_file_paths:
            with open(txt_file_path, 'r') as txt_file:
                lines = txt_file.readlines()
                
                for i in range(0, len(lines), 2):  # Loop through every pair of lines
                    utterance = lines[i]
                    logical_form = lines[i + 1]
                    csv_writer.writerow([row_id, utterance, logical_form])
                    row_id += 1  # Increment the row ID for the next pair

train_text_file_paths =["gen/train.txt", "gen_logical/train.txt", "para/train.txt", "para_logical/train.txt"]
train_csv_file_path = 'train.csv' 


test_text_file_paths = ["gen/test.txt", "gen_logical/test.txt", "para/test.txt", "para_logical/test.txt"]
test_csv_file_path = 'test.csv'

validation_text_file_paths = ["gen/val.txt", "gen_logical/val.txt", "para/val.txt", "para_logical/val.txt"]
validation_csv_file_path = 'validation.csv'


# # generate the three csv files 
# txts_to_csv(train_text_file_paths, train_csv_file_path)
# txts_to_csv(test_text_file_paths, test_csv_file_path)
# txts_to_csv(validation_text_file_paths, validation_csv_file_path)

from datasets import load_dataset

dataset = load_dataset('csv', data_files={
    'train': 'train.csv',
    'validation': 'validation.csv',
    'test': 'test.csv'
})

dataset.push_to_hub("robot_commands", private=True) # push our dataset to the hf hub 


