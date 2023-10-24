from datasets import DatasetDict, Dataset
import uuid

def read_files_to_dicts(file_paths):
    output_dicts = []

    for file_path in file_paths:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        for i in range(0, len(lines), 2):
            command = lines[i].strip()
            logical_form = lines[i + 1].strip()

            pair_dict = {
                "command": command,
                "logical_form": logical_form
            }
            output_dicts.append(pair_dict)

    return output_dicts

def generate_dataset_dict(file_lists):
    dataset_splits = {}
    
    for split, files in file_lists.items():
        output_dicts = read_files_to_dicts(files)

        id_translation_list = [{"id": str(uuid.uuid4()), "translation": item} for item in output_dicts]

        dataset_splits[split] = Dataset.from_dict({
            "id": [x['id'] for x in id_translation_list],
            "translation": [x['translation'] for x in id_translation_list]
        })
        
    return DatasetDict(dataset_splits)

if __name__ == "__main__":
    file_lists = {
        "train": ["gen/train.txt", "gen_logical/train.txt", "para/train.txt", "para_logical/train.txt"], 
        "test": ["gen/test.txt", "gen_logical/test.txt", "para/test.txt", "para_logical/test.txt"], 
        "validation": ["gen/val.txt", "gen_logical/val.txt", "para/val.txt", "para_logical/val.txt"]
    }
    
    dataset_dict = generate_dataset_dict(file_lists)

    # dataset_dict.push_to_hub("ezishiri/robot_commands_dataset") # push your dataset to HF for ease of access 

    print(dataset_dict['train'][0]) # make sure things are formatted correctly!
