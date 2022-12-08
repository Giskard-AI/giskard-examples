"""Main module."""
import pandas as pd
import os
import json
import pickle
import warnings
warnings.filterwarnings("ignore")

from giskard import GiskardClient
import sys

if __name__ == "__main__":

    model_date = os.listdir('trained_model')[0]

    trained_model_path='trained_model'

    model_filename = trained_model_path+'/'+model_date+'/logistic_regression_model.pkl'
    test_data_filename = trained_model_path+'/'+model_date+'/test_data.zip'
    clf_logistic_regression = pickle.load(open(model_filename, 'rb'))
    test_data = pd.read_pickle(test_data_filename, compression='zip')

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

    url = "http://dev.giskard.ai" #if Giskard is installed locally (for installation, see: https://docs.giskard.ai/start/guides/installation)
    token = os.environ['API_KEY'] #you can generate your API token in the Admin tab of the Giskard application (for installation, see: https://docs.giskard.ai/start/guides/installation)

    client = GiskardClient(url, token)

    # your_project = client.create_project("project_key", "PROJECT_NAME", "DESCRIPTION")
    # Choose the arguments you want. But "project_key" should be unique and in lower case
    try:
        credit_scoring = client.create_project("credit_scoring_deployment", "German Credit Scoring", "Project to predict if user will default")
    except:
        # If you've already created a project with the key "credit-scoring" use
        credit_scoring = client.get_project("credit_scoring_deployment")

    model_id, ds_id = credit_scoring.upload_model_and_df(
        prediction_function=clf_logistic_regression.predict_proba, # Python function which takes pandas dataframe as input and returns probabilities for classification model OR returns predictions for regression model
        model_type='classification', # "classification" for classification model OR "regression" for regression model
        df=test_data, # the dataset you want to use to inspect your model
        column_types=column_types, # A dictionary with columns names of df as key and types(category, numeric, text) of columns as values
        target='default', # The column name in df corresponding to the actual target variable (ground truth).
        feature_names=list(feature_types.keys()), # List of the feature names of prediction_function
        classification_labels=clf_logistic_regression.classes_ ,  # List of the classification labels of your prediction
        model_name=model_date, # Name of the model
        dataset_name='test_data' # Name of the dataset
    )

    test_suite_id = credit_scoring.list_test_suites()[0]['id']
    test_result = credit_scoring.execute_test_suite(
        test_suite_id=test_suite_id,
        model_id=model_id)

    passed_tests_cnt=0
    for test in test_result:
        if test['status'] == 'PASSED':
            passed_tests_cnt+=1

    PASSED = passed_tests_cnt/len(test_result)*1. > 0.5

    if PASSED:
        with open('trained_model/'+model_date+'/Giskard_tests.json', 'w', encoding='utf-8') as f:
            json.dump(test_result, f, ensure_ascii=False, indent=4)

        print(f'::set-output name=giskard_status::Passed')
        print(passed_tests_cnt/len(test_result)*100.,"> 50% of the tests passed. The model is verified!")

    else:
        print(f'::set-output name=giskard_status::Not Passed')
        raise RuntimeError(passed_tests_cnt/len(test_result)*100.,"< 50% of the tests passed. The model is not verified!")