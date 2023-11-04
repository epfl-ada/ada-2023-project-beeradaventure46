def convert_txt_to_csv(dataset_path:str = dataset_path, input_file:str=None, export:bool=False, file_name:str=None):
    """
    Converts a txt file to a csv file.

    Parameters
    ----------
    input_file : str
        The name of the txt file to be converted.
    export : bool
        Whether to export the csv file.
    file_name : str
        The name of the csv file to be exported. If None, the name of the txt file will be used.
    """

    # Define the file path
    file_path = dataset_path + input_file

    # Get the total number of lines in the file
    with io.open(file_path, 'r', encoding='utf-8') as f:
        total_lines = sum(1 for _ in f)
    print(f'Total number of lines: {total_lines}')

    # Initialize an empty dictionary to store the data
    data_dict = {}
    current_key = None
    
    # Use tqdm to visualize progress
    with io.open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in tqdm(lines, total=total_lines, desc='Processing Lines'):
            line = line.strip()
            if line:  # Skip empty lines
                key, value = line.split(':', 1)
                data_dict.setdefault(key.strip(), []).append(value.strip())
                current_key = key
    
    print('Finished processing lines.')
    
    # Create a DataFrame from the dictionary
    file_df = pd.DataFrame(data_dict)
    print('Created DataFrame.')
    
    if export:
        # export the df to csv
        if file_name is None:
            file_name = input_file.split('.')[0]

        output_path = dataset_path + file_name + '.csv'
        file_df.to_csv(output_path, index=False)
        print(f'File exported to {output_path}')
    else:
        print('File not exported.')
    
    return file_df