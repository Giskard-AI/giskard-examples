"""Main module."""
import os
os.environ['GSK_URL']="https://dev.giskard.ai/"
os.environ['GSK_TOKEN']="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInRva2VuX3R5cGUiOiJBUEkiLCJhdXRoIjoiUk9MRV9BRE1JTixST0xFX0FJVEVTVEVSIiwiZXhwIjoxNjgzNTQxNjI5fQ.7CXD98Yil36eaHHJuTxwjY_5vEIT8BcyWxD9Gk3U-HI"
os.environ['GSK_PROJECT_KEY']="test"
os.environ['GSK_PROJECT_NAME']="test"
os.environ['GSK_PROJECT_DESCRIPTION']="test"
import warnings
warnings.filterwarnings("ignore")

from giskard import GiskardClient

if __name__ == "__main__":

    url = os.environ['GSK_URL'] # read from https://github.com/Giskard-AI/giskard-examples secrets
    token = os.environ['GSK_TOKEN'] # read from https://github.com/Giskard-AI/giskard-examples secrets

    client = GiskardClient(url, token)

    try:
        credit_scoring = client.create_project(os.environ['GSK_PROJECT_KEY'], os.environ['GSK_PROJECT_NAME'], os.environ['GSK_PROJECT_DESCRIPTION'])
        print(f"Your project \"{os.environ['GSK_PROJECT_KEY']}\" is now created on {url}")
    except:
        credit_scoring = client.get_project(os.environ['GSK_PROJECT_KEY'])
        print(f"Your project \"{os.environ['GSK_PROJECT_KEY']}\" has already been created on {url}")

    try:
        test_suite_id = credit_scoring.list_test_suites()[0]['id']
        print("There's already a test suite created")
    except:
        print(f"Before the release of the test-API v2.0, you would need to create a test suite yourself from the \
              {url} in the project \"{os.environ['GSK_PROJECT_KEY']}\" in order for the deployment to work")
