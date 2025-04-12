import sys
from dataclasses import dataclass
import os 
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.mlproject.utils import save_object


from src.mlproject.exception import CustomException
from src.mlproject.logger import logging

import os


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
        
    def get_data_transformation_object(self):
        '''
        this function is reponsible for data Transformation
        '''  
        try:
            
            numerical_features = ['writing_score', 'reading_score']
            categorical_columns = ['gender', 'race/ethnicity', 
                                   'parental_level_of_education',
                                   'lunch', 'test_preparation_course']
            num_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])
            cat_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler", StandardScaler(with_mean = False))
            ])
            
            logging.info(f'Categorical columns: {categorical_columns}')
            logging.info(f'Numerical columns: {numerical_columns}')
            
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_features),
                    ("cat_pipeline", cat_pipeline, categorical_columns)
                ]
            )
            
            return preprocessor
            
            
        except Exception as e:
            raise CustomException(e, sys)
    def initiate_data_transormation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.into("Reading train  and test file  ")
            
            preprocessing_obj = self.get_data_transformation_object()
            
            target_column_name = 'math_score'
            numerical_features = ['writing_score', 'reading_score']
            
            #divide the train dataset to independent and feature
            
            input_features_train_df = train_df.drop(columns=[target_colums_name],axis = 1)
            target_feature_train_df = train_df[target_column_name]
            
            #divide the train dataset to independent and feature
            
            input_features_test_df = test_df.drop(columns=[target_colums_name],axis = 1)
            target_feature_train_df = test_df[target_column_name]
            
            logging.info("Applying preprocessing object on training and testing dataframe")
            input_features_train_arr= preprocessing_obj.fit(input_features_train_df)
            input_features_test_arr = preprocessing_obj.fit(input_features_test_df)
            
            train_arr = np.c_[
                input_features_train_arr, np.array(target_feature_train_df)
                ]
            test_arr = np.c_[input_features_test_arr, np.array(target_feature_train_df)
            ]
            logging.info("Saved preprocessing object")
            
            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )
            return  (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path 
            )
            
            
        except Exception as e:
            raise CustomException(e, sys)
        
            