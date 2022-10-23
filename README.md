<p align="center">
  <img alt="giskardlogo" src="https://raw.githubusercontent.com/Giskard-AI/giskard/main/readme/Logo_full_darkgreen.png">
</p>
<h1 align="center" weight='300' >Open-Source CI/CD for ML teams</h1>
<h3 align="center" weight='300' >Eliminate AI bias in production. Deliver ML products, better & faster</h3>
<p align="center">
   <a href="https://github.com/Giskard-AI/giskard/releases">
      <img alt="GitHub release" src="https://img.shields.io/github/v/release/Giskard-AI/giskard">
  </a>
 <a href="https://github.com/Giskard-AI/giskard/blob/main/LICENSE">
     <img alt="GitHub" src="https://img.shields.io/badge/License-Apache_2.0-blue.svg">
 </a>
  <a href="https://github.com/Giskard-AI/giskard/actions/workflows/build.yml">
    <img alt="build" src="https://github.com/Giskard-AI/giskard/actions/workflows/build.yml/badge.svg?branch=main"/>
 </a>
  <a href="https://gisk.ar/discord">
    <img alt="Giskard on Discord" src="https://img.shields.io/discord/939190303397666868?label=Discord"/>
  </a>
</p>
<h3 align="center">
   <a href="https://docs.giskard.ai/"><b>Documentation</b></a> &bull;
   <a href="https://www.giskard.ai/knowledge-categories/blog/?utm_source=github&utm_medium=github&utm_campaign=github_readme&utm_id=readmeblog"><b>Blog</b></a> &bull;  
  <a href="https://www.giskard.ai/?utm_source=github&utm_medium=github&utm_campaign=github_readme&utm_id=readmeblog"><b>Website</b></a> &bull;
  <a href="https://gisk.ar/discord"><b>Discord Community</b></a> &bull;
  <a href="https://www.giskard.ai/about?utm_source=github&utm_medium=github&utm_campaign=github_readme&utm_id=readmeblog#advisors"><b>Advisors</b></a>
 </h3>
<br />

# Giskard demo notebooks
We have built this repository to help you in the process of integrating Giskard by providing multiple notebooks. This repository has various notebooks which will help you to:
1. Create an ML model using open data
2. Create a project on Giskard 
3. Upload the model & data in Giskard


# How to navigate through this repository:
#### Here are the tags that we use to describe the content of each notebook:
1. Model libraries:
   #pytorch #tensorflow #scikit-learn #logistic_regression #random_forest #knn #transformers #huggingface #bert #roberta
2. How the prediction function is called:
   1. Pipeline: Models are created using #pipeline
   2. Wrapped Functions: Models use the traditional way of the whole process of data transformation and prediction using 
   python #wrapped_function
3. Data Types:
   1. #category_data
   2. #numeric_data
   3. #text_data
4. Model Type:
   1. #classification
   2. #regression


# Example Database: 
| Notebook                                                                                                                                                                | Tags                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [Credit Scoring Classification Model](https://github.com/Giskard-AI/demo-notebooks/blob/main/Credit%20scoring%20classification%20model.ipynb)                           | #scikit-learn #logistic_regression #random_forest #classification #category_data  #numeric_data #pipeline                                          |
| [Email Classification Model](https://github.com/Giskard-AI/demo-notebooks/blob/main/Email%20Classification%20Model.ipynb)                                               | #scikit-learn #nltk #transformers #huggingface #pytorch #bert #classification #text_data #category_data  #numeric_data #pipeline #wrapped_function |
| [House Pricing Regression Model](https://github.com/Giskard-AI/demo-notebooks/blob/main/House%20pricing%20regression%20model.ipynb)                                     | #scikit-learn #random_forest #catboost  #regression #category_data  #numeric_data #pipeline                                                        |
| [Sentiment Analysis For Twitter Data](https://github.com/Giskard-AI/demo-notebooks/blob/main/Sentiment_Analysis_for_Twitter_Data_using_Roberta.ipynb)                   | #transformers #huggingface #roberta #tweepy #datasets #classification #text_data #wrapped_function                                                 |
| [Iris Classification Using KNN](https://github.com/Giskard-AI/demo-notebooks/blob/main/Iris_demo.ipynb)                                                                 | #scikit-learn #knn #classification #numeric_data #category_data #wrapped_function #wrapped_function                                                |
| [Newspaper Data Classification](https://github.com/Giskard-AI/demo-notebooks/blob/main/Newspaper_classification.ipynb)                                                  | #pytorch #torchtext #dataloader #classification #text_data #wrapped_function                                                                       |
| [Text Classification Using Tensorflow Neural Network](https://github.com/Giskard-AI/demo-notebooks/blob/main/Text_classification_Using_Tensorflow_Neural_Network.ipynb) | #tensorflow #neural_network #classification #text_data #wrapped_function                                                                           |
| [Churn Telco Kaggle With transformers](https://github.com/Giskard-AI/examples/blob/main/Churn_Telco_Kaggle_with_transformers.ipynb)                                     | #scikit-learn #KNeighborsClassifier #LogisticRegression #RandomForestClassifier #GradientBoostingClassifier #classification #numeric_data #category_data #pipeline |
| [Churn Telco Kaggle Without transformers](https://github.com/Giskard-AI/examples/blob/main/Churn_Telco_Kaggle_without_transformers.ipynb)                               | #scikit-learn #KNeighborsClassifier #LogisticRegression #RandomForestClassifier #GradientBoostingClassifier #classification #numeric_data #category_data #wrapped_function #wrapped_function |
 
