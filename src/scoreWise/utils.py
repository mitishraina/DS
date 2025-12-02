import os
import sys
from src.scoreWise.exception import CustomException
from src.scoreWise.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
import pickle
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

load_dotenv()

HOST=os.getenv("HOST")
USER=os.getenv("USER")
PASS=os.getenv("PASS")
DATABASE=os.getenv("DB")

def read_db():
    logging.info("reading database started") 
    try:
        mydb=pymysql.connect(
            host=HOST,
            user=USER,
            password=PASS,
            db=DATABASE
        )
        logging.info("connection established with %s",mydb)
        df=pd.read_sql_query('Select * from student',mydb)
        print(df.head())
        
        return df
    except Exception as e:
        raise CustomException(e, sys)
    
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)        
            
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]
            
            print(f"Evaluating {list(models.keys())[i]} with parameters {para}") # added this for debugging

            gs = GridSearchCV(model, para, cv=3, error_score='raise')
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score
            
            print(f"Best parameters for {list(models.keys())[i]}: {gs.best_params_}")  #added this for debugging

        return report
    
    
    except Exception as e:
        raise CustomException(e, sys)