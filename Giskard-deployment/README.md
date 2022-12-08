[![Deployment workflow](https://github.com/rabah-khalek/Giskard-deployment/actions/workflows/deployment.yml/badge.svg)](https://github.com/rabah-khalek/Giskard-deployment/actions/workflows/deployment.yml)

# Giskard-deployment
Example of how to deploy the [credit scoring](https://github.com/Giskard-AI/giskard-examples/blob/main/Credit%20scoring%20classification%20model.ipynb) once it passes [Giskard](https://www.giskard.ai/)'s tests.

## Workflow
The deployment happens according to three steps:
- [Training](https://github.com/rabah-khalek/Giskard-deployment/blob/0f2902bf653adb04551f7be11a700e0e0e95f327/.github/workflows/deployment.yml#L5-L48): execution of `train.py` script every time a `push` occurs.
- [Testing](https://github.com/rabah-khalek/Giskard-deployment/blob/0f2902bf653adb04551f7be11a700e0e0e95f327/.github/workflows/deployment.yml#L50-L101): execution of `Giskard_test.py` script after the training is done. During this step, the model produced by `train.py` is uploaded to the Giskard UI (where the user can define his custom test suite). Then all the tests are performed. If at least 50% of the tests pass (this can be tuned [here](https://github.com/rabah-khalek/Giskard-deployment/blob/0f2902bf653adb04551f7be11a700e0e0e95f327/Giskard_test.py#L85) in `Giskard_test.py`), the model is tagged as verified.
- [Deployment](https://github.com/rabah-khalek/Giskard-deployment/blob/0f2902bf653adb04551f7be11a700e0e0e95f327/.github/workflows/deployment.yml#L103-L142): If the model is verified, it is committed to the repo under the folder `deployed_model` that contains:
  - a subfolder named as the date of the model training which itself contains: 
    - `logistic_regression_model.pkl`: a pickle of the verified model.
    - `test_data.zip`: a pandas dataframe that was used to verify the model.
    - `Giskard_tests.json`: a summary of all the tests and metrics that were run by Giskard.
    
<img width="950" alt="Screenshot 2022-12-08 at 15 54 18" src="https://user-images.githubusercontent.com/32709181/206478480-d3831099-ca5b-4a95-9282-598f6a433639.png">
