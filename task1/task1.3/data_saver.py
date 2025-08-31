#!/usr/bin/env python3
from pathlib import Path
import json

def data_saver(data: dict, data_format='json', file_name='output') -> bool:
    
    file_name += data_format  
    file_path = Path(file_name)

    try:
        if data_format == 'json':
            with file_path.open('w') as file:
                json.dump(data, file)  
                
        elif data_format == 'txt':
            with file_path.open('a') as file:  
                for key, value in data.items():
                    file.write(f"{key} = {value}\n")
        else:
            return False
    except Exception :
      
        return False

    return True


#test running code
if __name__ == "__main__":
    test_dict = {
        'Name': 'Jon',
        'Passport Number': 'A23B120',
        'Occupation': 'Airfoce Commander',
        'Married': True,
        'Age': 34
    }

    # save as json
    if data_saver(test_dict, 'json', 'output'):
        print("Saved as .JSON ")

    # save as txt
    if data_saver(test_dict, 'txt', 'output'):
        print("Saved as .TXT")
