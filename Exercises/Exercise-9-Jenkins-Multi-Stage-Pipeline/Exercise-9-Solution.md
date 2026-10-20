# Exercise 9: Jenkins Multi-Stage Pipeline

## Objective
To create and execute a Jenkins pipeline for a Python Flask application using multiple stages: Build, Test, Deploy, Run Application, and Test Application.

## Application
The Flask application displays the message:

`Hello, Jenkins Multi-Stage Pipeline!`

## Pipeline Stages

1. **Build:** Prepare the Python environment and install the required dependencies.
2. **Test:** Run unit tests to verify the Flask application's response.
3. **Deploy:** Copy the application into a mock deployment directory.
4. **Run Application:** Start the deployed application.
5. **Test Application:** Verify the application after deployment.

## Tools Used
- Jenkins
- Git and GitHub
- Python
- Flask
- Docker (if required for the build environment)

### Execution Results

The Jenkins multi-stage pipeline was executed successfully using the `python-agent` node.

All stages completed successfully:

1. **Checkout:** Retrieved the project from the GitHub repository.
2. **Build:** Installed Flask and its required dependencies.
3. **Test:** Executed the Python unit test successfully (`1 test, OK`).
4. **Deploy:** Copied `app.py`, `requirements.txt`, and `test_app.py` into the `python-app-deploy` directory.
5. **Run Application:** Verified the deployed application's functionality by running the unit test again.
6. **Test Application:** Confirmed that the Flask application returned HTTP status code `200` and the expected response: `Hello, Jenkins Multi-Stage Pipeline!`

**Final Status:** `SUCCESS`

### Conclusion

The exercise successfully demonstrated a Jenkins declarative pipeline for a Python Flask application. The pipeline automates code checkout, dependency installation, unit testing, deployment to a mock directory, and verification of the deployed application.


