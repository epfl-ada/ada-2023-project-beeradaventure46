import io
import time
import spacy
import nltk
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pyarrow.parquet as pq

from typing import List
from tqdm import tqdm
from textblob import TextBlob
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from spacy.tokens import Doc
from scipy.stats import ttest_ind
from textstat import flesch_reading_ease
from sklearn.linear_model import LinearRegression
from concurrent.futures import ThreadPoolExecutor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

dataset_path = './data/BeerAdvocate/'

### Part 1 
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
    
    # Use tqdm to visualize progress
    with io.open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in tqdm(lines, total=total_lines, desc='Processing Lines'):
            line = line.strip()
            if line:  # Skip empty lines
                key, value = line.split(':', 1)
                data_dict.setdefault(key.strip(), []).append(value.strip())
    
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

def convert_txt_to_parquet(dataset_path:str = dataset_path, input_file:str=None, export:bool=False, file_name:str=None):
    """
    Converts a txt file to a parquet file.

    Parameters
    ----------
    input_file : str
        The name of the txt file to be converted.
    export : bool
        Whether to export the parquet file.
    file_name : str
        The name of the parquet file to be exported. If None, the name of the txt file will be used.
    """

    # Define the file path
    file_path = dataset_path + input_file

    # Get the total number of lines in the file
    with io.open(file_path, 'r', encoding='utf-8') as f:
        total_lines = sum(1 for _ in f)
    print(f'Total number of lines: {total_lines}')

    # Initialize an empty dictionary to store the data
    data_dict = {}
    
    # Use tqdm to visualize progress
    with io.open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in tqdm(lines, total=total_lines, desc='Processing Lines'):
            line = line.strip()
            if line:  # Skip empty lines
                key, value = line.split(':', 1)
                data_dict.setdefault(key.strip(), []).append(value.strip())
    
    print('Finished processing lines.')
    
    # Create a DataFrame from the dictionary
    file_df = pd.DataFrame(data_dict)
    print('Created DataFrame.')
    
    if export:
        # export the df to csv
        if file_name is None:
            file_name = input_file.split('.')[0]
        # to parquet rather than csv
        output_path = dataset_path + file_name + '.parquet'
        file_df.to_parquet(output_path, index=False)
        print(f'File exported to {output_path}')
    else:
        print('File not exported.')
    
    return file_df

def show_missing(df: pd.DataFrame) -> None:
    """
    This function receives a dataframe and plots the percentage of missing values per column.
    It also prints, for each column with missing values, the number of missing values and
    the percentage of missing values. If there are no missing values, it prints a message saying so.

    Parameters:
    - df (pd.DataFrame): The input dataframe.

    Returns:
    - None
    """
    # check if there are any missing values
    if df.isna().sum().sum() == 0:
        print('There are no missing values in this dataset.')
        return
    else:
        # show the percentage of missing values per column
        plt.figure()
        (df.isna().sum() / len(df) * 100).plot(kind='barh', title='Percentage of missing values per column')
        plt.xlabel('Percentage of missing values')
        plt.show()

        missing_values = df.isnull().sum()
        total_values = df.shape[0]
        missing_percentage = missing_values / total_values * 100
        for col in df.columns:
            if missing_values[col] > 0:
                print("{:<25}: {:>5} missing values ({:.2f}%)".format(col, missing_values[col], missing_percentage[col]))


### Part 2


# Manual labelling
def display_review(df: pd.DataFrame) -> int or None:
    """
    Displays a review that has not been labelled yet and returns its index.

    Parameters:
    - df (pd.DataFrame): The input dataframe.

    Returns:
    - int or None: The index of the review to be displayed, or None if no more reviews to label.
    """
    # filter the dataframe to only include rows where 'true_serving_type' is 'unknown'
    df_not_set = df[df['true_serving_type'] == 'not_set']
    if len(df_not_set) == 0:
        print('No more reviews to label')
        return None
    else:
        # print the 'text' column of the first row with unknown serving type
        index = df_not_set.index[0]
        print(f"Review {index}:\n{df_not_set.loc[index, 'text']}")
        
        return index

def update_review_serving_type(df: pd.DataFrame, index: int or None) -> pd.DataFrame:
    """
    Changes the 'true_serving_type' column of the review with the given index.

    Parameters:
    - df (pd.DataFrame): The input dataframe.
    - index (int or None): The index of the review to update, or None if no review to update.

    Returns:
    - pd.DataFrame: The updated dataframe.
    """
    # ask the user to input the serving type
    if index is None:
        return df
    else:
        serving_type = input("Enter the serving type (bottle/can/draft/unknown): ")
        if serving_type not in ['bottle', 'can', 'draft', 'unknown']:
            print('Invalid serving type')
            return df
        else:
            # update the 'true_serving_type' column of the review with the given index
            df.loc[index, 'true_serving_type'] = serving_type
            return df     
        
def compute_accuracy(predictions: List[int], true_classes: List[int]) -> float:
    """
    Computes the accuracy of the predictions.

    Parameters:
    - predictions (List[int]): The predicted classes.
    - true_classes (List[int]): The true classes.

    Returns:
    - float: The accuracy of the predictions.
    """
    if len(predictions) != len(true_classes):
        raise ValueError("Length of predictions and true_classes must be the same.")

    correct_count = sum(pred == true_class for pred, true_class in zip(predictions, true_classes))
    total_count = len(predictions)

    accuracy = correct_count / total_count if total_count > 0 else 0.0
    print(f'correct_count: {correct_count}, total_count: {total_count}')
    return accuracy

def sentiment_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes a pandas dataframe as input and adds two columns to it: 'polarity' and 'subjectivity'.
    The 'polarity' column contains the polarity score of each review, which is a float between -1 and 1 indicating the sentiment of the review.
    The 'subjectivity' column contains the subjectivity score of each review, which is a float between 0 and 1 indicating the degree of subjectivity of the review.

    Parameters:
    - df (pd.DataFrame): The input dataframe.

    Returns:
    - pd.DataFrame: The dataframe with added 'polarity' and 'subjectivity' columns.
    """
    # Add 'polarity' and 'subjectivity' columns to the dataframe
    with tqdm(total=len(df)) as pbar:
        for index, row in df.iterrows():
            df.at[index, 'polarity'] = TextBlob(row['text']).sentiment.polarity
            # df.at[index, 'subjectivity'] = TextBlob(row['text']).sentiment.subjectivity
            pbar.update(1)
    return df

def compute_readability(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute the readability score of each review using the Flesch reading ease test.

    Parameters:
    - df (pd.DataFrame): The input dataframe.

    Returns:
    - pd.DataFrame: The dataframe with added 'readability_score' column.
    """
    with tqdm(total=len(df)) as pbar:
        for index, row in df.iterrows():
            df.at[index, 'readability_score'] = flesch_reading_ease(row['text'])
            pbar.update(1)
        return df