"""Main module."""
import pandas as pd
import os
import pickle
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
 
from sklearn import model_selection
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

if __name__ == "__main__":
    time = datetime.now()
    dt_string = time.strftime("%d-%m-%Y_%H.%M.%S")

    data_file = "data.csv"
    credit = pd.read_csv(data_file, sep=',',engine="python") #To download go to https://github.com/Giskard-AI/giskard-client/tree/main/sample_data/classification

    # Declare the type of each column in the dataset(example: category, numeric, text)
    column_types = {'default':"category",
                    'account_check_status':"category",
                    'duration_in_month':"numeric",
                    'credit_history':"category",
                    'purpose':"category",
                    'credit_amount':"numeric",
                    'savings':"category",
                    'present_employment_since':"category",
                    'installment_as_income_perc':"numeric",
                    'sex':"category",
                    'personal_status':"category",
                    'other_debtors':"category",
                    'present_residence_since':"numeric",
                    'property':"category",
                    'age':"numeric",
                    'other_installment_plans':"category",
                    'housing':"category",
                    'credits_this_bank':"numeric",
                    'job':"category",
                    'people_under_maintenance':"numeric",
                    'telephone':"category",
                    'foreign_worker':"category"}

    # feature_types is used to declare the features the model is trained on
    feature_types = {i:column_types[i] for i in column_types if i!='default'}

    # Pipeline to fill missing values, transform and scale the numeric columns
    columns_to_scale = [key for key in feature_types.keys() if feature_types[key]=="numeric"]
    numeric_transformer = Pipeline([('imputer', SimpleImputer(strategy='median')),
                                    ('scaler', StandardScaler())])

    # Pipeline to fill missing values and one hot encode the categorical values
    columns_to_encode = [key for key in feature_types.keys() if feature_types[key]=="category"]
    categorical_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore',sparse=False)) ])

    # Perform preprocessing of the columns with the above pipelines
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, columns_to_scale),
            ('cat', categorical_transformer, columns_to_encode)
        ]
    )

    # Pipeline for the model Logistic Regression
    clf_logistic_regression = Pipeline(steps=[('preprocessor', preprocessor),
                                              ('classifier', LogisticRegression(max_iter =1000))])

    # Split the data into train and test
    Y = credit['default']
    X = credit.drop(columns="default")
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.20,random_state = 30, stratify = Y)


    # Fit and score your model
    clf_logistic_regression.fit(X_train, Y_train)
    print("model score: ", clf_logistic_regression.score(X_test, Y_test))

    # Prepare data to upload on Giskard
    test_data = pd.concat([X_test, Y_test ], axis=1)

    # Dumping
    trained_model_path='trained_model'
    if not os.path.isdir(trained_model_path):
        os.system('mkdir '+trained_model_path)

    if not os.path.isdir(trained_model_path+'/'+dt_string):
        os.system('mkdir '+trained_model_path+'/'+dt_string)

    model_filename = trained_model_path+'/'+dt_string+'/logistic_regression_model.pkl'
    test_data_filename = trained_model_path+'/'+dt_string+'/test_data.zip'
    pickle.dump(clf_logistic_regression, open(model_filename, 'wb'))
    test_data.to_pickle(test_data_filename, compression='zip')
