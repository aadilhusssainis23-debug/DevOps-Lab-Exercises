# Exercise 7: Jenkins CI Automation

## Objective
To understand Continuous Integration (CI) and configure a Jenkins pipeline to retrieve and verify code from a GitHub repository.

## Implementation

### 1. Jenkins Setup
Used the existing Jenkins container running through Docker on port 8080.

### 2. Jenkins Pipeline
Created a pipeline job named `Exercise-7-CI-Automation`.

### 3. Checkout Stage
Jenkins cloned the `main` branch from the personal GitHub repository.

### 4. Git Verification Stage
The pipeline checked the installed Git version and verified the repository's working-tree status.

### 5. Repository Verification Stage
The pipeline checked for the following files:
- `README.md`
- `Exercises/Exercise-6-Delivery-Monitoring/delivery_metrics.py`
- `Exercises/Exercise-6-Delivery-Monitoring/prometheus.yml`

### 6. Build Result
The Jenkins pipeline completed successfully with the status `SUCCESS`.

## Platform Note
The pipeline runs in the existing Jenkins Docker container on macOS. Python-based tests were not included because Python 3 was unavailable in the container and package installation encountered repository download errors.

## Conclusion
A basic Jenkins CI pipeline was configured to check out a GitHub repository, verify Git, and confirm that required project files exist. The successful build demonstrated that Jenkins can retrieve and validate the repository.
