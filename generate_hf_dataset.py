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
        "train": ["train_file1.txt", "train_file2.txt"], 
        "test": ["test_file1.txt"], 
        "validation": ["validation_file1.txt"]
    }
    
    dataset_dict = generate_dataset_dict(file_lists)
    
    print(dataset_dict)
