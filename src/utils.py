def read_files_to_df(folder_path):
    dfs = []

    # Iterate over the files in the folder
    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            file_path = os.path.join(folder_path, file)
            # Read the CSV file into a dataframe and append it to the list
            dfs.append(pd.read_csv(file_path))

    # Concatenate all the dataframes into a single dataframe
    return pd.concat(dfs, ignore_index=True)


def create_acronym(category):
    # Split the category by underscores and take the first letter of each word after 'STATEMENT_CATEGORY'
    return ''.join([word[0] for word in category.split('_')[2:]])